#!/usr/bin/env python3
"""Offline integrity gate; --online explicitly verifies GitHub release facts."""
import argparse
from datetime import date
from html.parser import HTMLParser
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

from catalog_content import BEGIN, END, LANGUAGES, catalog_section, evidence_document

SLUGS = {'liquid-glass-tab-bars', 'adaptive-app-shell', 'live-activity-dynamic-island-kit', 'mac-menu-bar-command-kit', 'resizelint'}
TYPES = {'release-metadata', 'source-review', 'published-ci', 'artifact-inspection', 'native-test', 'device-test', 'independent-signing'}
VERSION = r'(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?'
SHA = r'[0-9a-f]{40}'


class GateError(Exception):
    pass


def require(condition, field, message):
    if not condition:
        raise GateError(f'catalog.json: {field}: {message}')


def shape(value, keys, field, optional=()):
    require(isinstance(value, dict), field, 'expected object')
    require(set(keys).issubset(value) and set(value).issubset(set(keys) | set(optional)), field, f'expected fields: {", ".join(keys)}')


def nonempty(value, field):
    require(isinstance(value, str) and bool(value.strip()), field, 'expected nonempty string')


def bilingual(value, field):
    shape(value, ('en', 'ru'), field)
    for lang in ('en', 'ru'):
        nonempty(value[lang], field + '.' + lang)


def iso_date(value, field):
    nonempty(value, field)
    try:
        parsed = date.fromisoformat(value)
        require(parsed.isoformat() == value, field, 'use YYYY-MM-DD')
    except ValueError:
        raise GateError(f'catalog.json: {field}: invalid ISO date') from None


def local_path(root, value, field):
    nonempty(value, field)
    pure = PurePosixPath(value)
    require(not pure.is_absolute() and '..' not in pure.parts and '\\' not in value and ':' not in value, field, f'unsafe relative path: {value}')
    target = (root / value).resolve()
    require(target.is_relative_to(root), field, f'path escapes catalog root: {value}')
    require(target.is_file(), field, f'missing local file: {value}')
    return target


def https_url(value, field):
    nonempty(value, field)
    parsed = urlsplit(value)
    require(parsed.scheme == 'https' and parsed.netloc == 'github.com' and not parsed.username and not parsed.password, field, 'expected a public https://github.com URL')


def validate_schema(data, root):
    shape(data, ('schema_version', 'checked_on', 'media', 'products'), '$')
    require(type(data['schema_version']) is int and data['schema_version'] == 1, 'schema_version', 'expected 1')
    iso_date(data['checked_on'], 'checked_on')
    require(isinstance(data['products'], list) and len(data['products']) == 5, 'products', 'expected five records')
    slugs = []
    for i,p in enumerate(data['products']):
        f = f'products[{i}]'
        shape(p, ('slug','kind','name','url','release','minimum_os','toolchain','scenario','unnecessary','summary','dependencies','claims','limits','verification','evidence','preview','routes'), f)
        for key in ('slug','name','minimum_os','toolchain'):
            nonempty(p[key], f+'.'+key)
        slugs.append(p['slug'])
        require(p['kind'] == ('tool' if p['slug']=='resizelint' else 'template'), f+'.kind', 'expected four templates and one separate tool')
        https_url(p['url'], f+'.url')
        require(re.fullmatch(r'https://github.com/[\w.-]+/[\w.-]+', p['url']), f+'.url', 'expected repository URL')
        for key in ('scenario','unnecessary','summary'):
            bilingual(p[key], f+'.'+key)
        r = p['release']
        shape(r, ('tag','commit','status'), f+'.release')
        require(isinstance(r['tag'],str) and re.fullmatch(VERSION,r['tag']), f+'.release.tag', 'expected an exact semantic release tag, not latest/main')
        require(isinstance(r['commit'],str) and re.fullmatch(SHA,r['commit']), f+'.release.commit', 'expected immutable 40-character lowercase SHA')
        require(r['status'] in ('released','preview'), f+'.release.status', 'expected released or preview')
        require(isinstance(p['dependencies'],list) and all(isinstance(d,str) and d for d in p['dependencies']),f+'.dependencies','expected dependency names')
        v = p['verification']
        shape(v, ('type','date','scope'), f+'.verification')
        require(v['type'] in TYPES, f+'.verification.type','unknown verification type')
        iso_date(v['date'], f+'.verification.date')
        require(v['date'] <= data['checked_on'], f+'.verification.date','cannot be later than checked_on')
        bilingual(v['scope'], f+'.verification.scope')
        require(isinstance(p['evidence'],list) and bool(p['evidence']),f+'.evidence','expected evidence records')
        by_id = {}
        for j,e in enumerate(p['evidence']):
            ef = f+f'.evidence[{j}]'
            shape(e, ('id','type','date','sources'), ef, ('sha256',))
            nonempty(e['id'],ef+'.id')
            require(e['id'] not in by_id,ef+'.id','duplicate evidence ID')
            require(e['type'] in TYPES,ef+'.type','unknown verification type')
            iso_date(e['date'],ef+'.date')
            require(e['date'] <= data['checked_on'],ef+'.date','cannot be later than checked_on')
            require(isinstance(e['sources'],list) and bool(e['sources']),ef+'.sources','evidence needs source URLs')
            for source in e['sources']:
                https_url(source,ef+'.sources')
                require(source.startswith(p['url']+'/'),ef+'.sources','source must belong to this product')
            require(any('/'+r['commit'] in source for source in e['sources']),ef+'.sources','evidence must identify the immutable product commit')
            if 'sha256' in e:
                require(isinstance(e['sha256'],str) and re.fullmatch(r'[0-9a-f]{64}',e['sha256']),ef+'.sha256','expected SHA-256')
            by_id[e['id']] = e
        require('release' in by_id and p['url']+'/releases/tag/'+r['tag'] in by_id['release']['sources'],f+'.release.tag','release evidence must match tag')
        require(v['type'] in {e['type'] for e in p['evidence']},f+'.verification.type','no matching evidence')
        for key in ('claims','limits'):
            require(isinstance(p[key],list) and bool(p[key]),f+'.'+key,'expected nonempty list')
            for j,c in enumerate(p[key]):
                cf = f+f'.{key}[{j}]'
                shape(c, ('text','evidence'),cf)
                bilingual(c['text'],cf+'.text')
                require(isinstance(c['evidence'],list) and bool(c['evidence']) and all(isinstance(e,str) and e in by_id for e in c['evidence']),cf+'.evidence','claim needs valid provenance IDs')
                claim_types = {by_id[e]['type'] for e in c['evidence']}
                text = c['text']['en'].lower()
                for pattern,needed in ((r'^(?:independently )?(?:device[- ]verified|tested on (?:physical )?devices)', 'device-test'), (r'^independently (?:signed|notarized|gatekeeper[- ]verified)', 'independent-signing')):
                    require(not re.search(pattern,text) or needed in claim_types,cf+'.evidence',f'strong claim requires {needed} evidence')
        pr = p['preview']
        shape(pr, ('path','width','alt','source'),f+'.preview', ('motion','frame'))
        local_path(root,pr['path'],f+'.preview.path')
        require(type(pr['width']) is int and 100<=pr['width']<=1000,f+'.preview.width','expected 100–1000 CSS pixels')
        bilingual(pr['alt'],f+'.preview.alt')
        https_url(pr['source'],f+'.preview.source')
        require(re.search(r'/blob/'+SHA+r'/Assets/',pr['source']),f+'.preview.source','preview needs immutable catalog capture provenance')
        if 'motion' in pr:
            local_path(root,pr['motion'],f+'.preview.motion')
            require(type(pr.get('frame')) is int and pr['frame']>=0,f+'.preview.frame','expected original zero-based frame index')
        routes = p['routes']
        shape(routes, ('issues','security_policy'),f+'.routes')
        require(routes['issues']==p['url']+'/issues/new/choose',f+'.routes.issues','expected product issue route')
        require(routes['security_policy']==p['url']+'/blob/main/SECURITY.md',f+'.routes.security_policy','link the current upstream policy, not an assumed private endpoint')
    require(set(slugs)==SLUGS and len(set(slugs))==5,'products.slug','expected five unique known product slugs')
    m = data['media']
    shape(m, ('baseline_revision','baseline_raster_bytes','baseline_all_local_bytes','max_bytes','shared','baseline'),'media')
    require(m['baseline_revision']=='4828708e88c8410f1d870d6aef942058b1a56e42','media.baseline_revision','expected measured original catalog revision')
    require(m['baseline_raster_bytes']==8835016 and m['baseline_all_local_bytes']==8838071,'media.baseline','baseline totals must match recorded measurement')
    require(type(m['max_bytes']) is int and 0<m['max_bytes']<=5301009,'media.max_bytes','cap may not exceed 5,301,009 bytes')
    require(isinstance(m['shared'],list),'media.shared','expected local shared image paths')
    for asset in m['shared']:
        local_path(root,asset,'media.shared')
    require(isinstance(m['baseline'],list),'media.baseline','expected original per-file measurements')
    for j,item in enumerate(m['baseline']):
        shape(item,('path','bytes'),f'media.baseline[{j}]')
        require(type(item['bytes']) is int and item['bytes']>0,f'media.baseline[{j}].bytes','expected measured bytes')
        local_path(root,item['path'],f'media.baseline[{j}].path')
    require(sum(item['bytes'] for item in m['baseline'])==8838071,'media.baseline','per-file baseline must match total')


class Markup(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.images, self.anchors = [], [], set()
        self.feed(text)

    def handle_starttag(self,tag,attrs):
        attrs = dict(attrs)
        for key in ('id','name'):
            if key in attrs:
                self.anchors.add(attrs[key])
        if tag=='a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag=='img':
            self.images.append((attrs.get('src',''),attrs.get('alt','')))


def anchors(text):
    result = Markup(text).anchors
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        result.add(''.join(c for c in heading.lower() if c==' ' or c in '-_' or unicodedata.category(c)[0] in 'LN').replace(' ','-'))
    return result


def read(root, name):
    try:
        return (root/name).read_text(encoding='utf-8')
    except (OSError,UnicodeError) as exc:
        raise GateError(f'{name}: cannot read file ({type(exc).__name__})') from None


def validate_documents(data,root):
    displayed = set()
    expected = set(data['media']['shared']) | {p['preview']['path'] for p in data['products']}
    for lang,name in LANGUAGES.items():
        text = read(root,name)
        if text.count(BEGIN)!=1 or text.count(END)!=1:
            raise GateError(f'{name}: catalog: expected one generated region')
        region = text[text.index(BEGIN):text.index(END)+len(END)]
        if region != catalog_section(data,lang):
            raise GateError(f'{name}: catalog facts differ from catalog.json; run python3 Scripts/render-catalog.py')
        if re.search(r'<\s*(?:table|th|td)\b',text,re.I):
            raise GateError(f'{name}: presentation: HTML tables are not allowed')
        outside = text[:text.index(BEGIN)] + text[text.index(END)+len(END):]
        if re.search(r'\b(?:fully verified|production[- ]ready|device[- ]verified|stable \d)|полностью проверен|полной проверки',outside,re.I):
            raise GateError(f'{name}: claims: put strong guarantees in the manifest with scoped provenance')
        for src,alt in Markup(text).images:
            if not alt.strip():
                raise GateError(f'{name}: image.alt: missing accessible description for {src}')
            if not urlsplit(src).scheme:
                displayed.add(src)
        for src,alt in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',text):
            if not src.strip():
                raise GateError(f'{name}: image.alt: missing accessible description')
            if not urlsplit(alt).scheme:
                displayed.add(alt)
    require(displayed==expected,'media.displayed','README image set differs from declared previews/shared assets')
    media_bytes = sum(local_path(root,p,'media.displayed').stat().st_size for p in displayed)
    require(media_bytes<=data['media']['max_bytes'],'media.max_bytes',f'{media_bytes:,} embedded bytes exceed {data["media"]["max_bytes"]:,}')
    if read(root,'Docs/Catalog-evidence.md') != evidence_document(data):
        raise GateError('Docs/Catalog-evidence.md: claims: differs from manifest evidence; regenerate')
    config = read(root,'.github/ISSUE_TEMPLATE/config.yml')
    urls = re.findall(r'^\s+url:\s+(https://\S+)\s*$',config,re.M)
    contributing, security = read(root,'CONTRIBUTING.md'),read(root,'SECURITY.md')
    for p in data['products']:
        for filename,text,key in (('.github/ISSUE_TEMPLATE/config.yml',urls,'issues'),('CONTRIBUTING.md',contributing,'issues'),('SECURITY.md',security,'security_policy')):
            if p['routes'][key] not in text:
                raise GateError(f'{filename}: {p["name"]}.routes.{key}: missing {p["routes"][key]}')
    for file in sorted(root.glob('*.md')) + sorted((root/'Docs').glob('*.md')):
        text = file.read_text(encoding='utf-8')
        links = [m.group(1) for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',text)]
        markup = Markup(text)
        links += markup.links + [src for src,_ in markup.images]
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            target = file if not path else local_path(root,file.parent.relative_to(root).joinpath(path).as_posix(),str(file.relative_to(root))+'.link')
            if parsed.fragment and target.suffix=='.md' and unquote(parsed.fragment) not in anchors(target.read_text(encoding='utf-8')):
                raise GateError(f'{file.relative_to(root)}: anchor: missing {link}')
    git = subprocess.run(['git','-C',str(root),'ls-files'],capture_output=True,text=True)
    if git.returncode==0:
        for path in git.stdout.splitlines():
            if re.search(r'(^|/)(\.DS_Store|Thumbs\.db|xcuserdata|DerivedData|\.build|__pycache__)(/|$)|\.(xcuserstate|xccheckout|pyc)$',path):
                raise GateError(f'{path}: hygiene: generated or personal files must not be tracked')
    return media_bytes


def api_json(base,path,timeout):
    headers = {'Accept':'application/vnd.github+json','User-Agent':'Apple-Design-Templates-catalog-validator','X-GitHub-Api-Version':'2022-11-28'}
    # Never send an environment credential to the loopback failure-fixture server.
    if base=='https://api.github.com' and os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    request = Request(base+'/'+path,headers=headers)
    with urlopen(request,timeout=timeout) as response:
        return json.load(response)


def verify_online(data,base,timeout):
    incomplete, invalid = False,False
    for p in data['products']:
        repo = p['url'].removeprefix('https://github.com/')
        tag = p['release']['tag']
        try:
            prefix = 'repos/'+repo
            release = api_json(base,prefix+'/releases/tags/'+quote(tag,safe=''),timeout)
            commit = api_json(base,prefix+'/commits/'+quote(tag,safe=''),timeout)
            if release.get('draft') or release.get('tag_name')!=tag or commit.get('sha')!=p['release']['commit'] or (p['release']['status']=='released' and release.get('prerelease')):
                print(f'ERROR {p["slug"]}: release.tag/commit/status: remote facts differ')
                invalid = True
                continue
            latest = api_json(base,prefix+'/releases/latest',timeout)
            print(f'VERIFIED {p["slug"]}: {tag} @ {commit["sha"]}')
            if latest.get('tag_name')!=tag:
                print(f'NOTICE {p["slug"]}: newer published release {latest.get("tag_name")}; review it before changing catalog facts')
        except HTTPError as exc:
            if exc.code==404:
                print(f'ERROR {p["slug"]}: release.tag: release/commit endpoint returned 404')
                invalid = True
            else:
                print(f'UNVERIFIED {p["slug"]}: GitHub HTTP {exc.code}; remote state not established')
                incomplete = True
        except (URLError,OSError,TimeoutError,ValueError,KeyError,TypeError) as exc:
            print(f'UNVERIFIED {p["slug"]}: {type(exc).__name__}; remote state not established')
            incomplete = True
    if invalid:
        return 1
    if incomplete:
        return 2
    print('ONLINE PASS: exact release tags and immutable commits verified; no runtime acceptance claimed')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--online',action='store_true')
    parser.add_argument('--api-base',default='https://api.github.com',help='GitHub API; loopback URL allowed for failure fixtures')
    parser.add_argument('--network-timeout',type=float,default=10)
    args = parser.parse_args()
    base = args.api_base.rstrip('/')
    if base!='https://api.github.com' and (urlsplit(base).scheme!='http' or urlsplit(base).hostname not in ('127.0.0.1','localhost','::1')):
        parser.error('--api-base must be the GitHub API or an HTTP loopback failure fixture')
    if args.network_timeout<=0:
        parser.error('--network-timeout must be positive')
    root = args.root.resolve()
    try:
        data = json.loads(read(root,'catalog.json'))
        validate_schema(data,root)
        media_bytes = validate_documents(data,root)
    except (GateError,json.JSONDecodeError) as exc:
        print(f'ERROR {exc}',file=sys.stderr)
        return 1
    print(f'OFFLINE PASS: 5 records; EN/RU, provenance, routes, links; {media_bytes:,}/{data["media"]["max_bytes"]:,} embedded media bytes')
    return verify_online(data,base,args.network_timeout) if args.online else 0


if __name__ == '__main__':
    raise SystemExit(main())

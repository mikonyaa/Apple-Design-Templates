"""Deterministic bilingual catalog sections, using only the standard library."""
from html import escape

BEGIN = '<!-- catalog:begin -->'
END = '<!-- catalog:end -->'
LANGUAGES = {'en': 'README.md', 'ru': 'README.ru.md'}


def catalog_section(data, lang):
    ru = lang == 'ru'
    lines = [BEGIN, '', '## Как выбрать' if ru else '## Choose by outcome', '']
    for p in data['products']:
        lines.append(f"- **{p['scenario'][lang]}** → [{p['name']}](#{p['slug']}) · {p['release']['tag']}")
    lines += ['',
        'Выбирайте минимальный package, который решает вашу задачу. Четыре UI-шаблона независимы; ResizeLint можно использовать отдельно.' if ru else
        'Pick the smallest package that owns your problem. The four UI templates are independent; ResizeLint can be used separately.',
        '',
        '**Released** означает опубликованный release с указанным tag. **Preview** — ещё не опубликованный или prerelease-проект. **Verified scope** указывает только реально проведённую проверку; source review и CI не подтверждают device или production behavior.' if ru else
        '**Released** means a published release at the named tag. **Preview** means unreleased or prerelease work. **Verified scope** states only the checks actually performed; source review and CI do not establish device or production behavior.',
        '', '## Шаблоны' if ru else '## Templates', '']
    for p in data['products']:
        if p['kind'] == 'tool':
            lines += ['## Инструмент разработчика' if ru else '## Developer tool', '']
        release = p['release']
        label = 'Released' if release['status'] == 'released' else 'Preview'
        preview = p['preview']
        target = preview.get('motion', p['url'])
        lines += [f'<a name="{p["slug"]}"></a>', '', f'### {p["name"]}', '',
            f"> **{label} {release['tag']}** · {p['minimum_os']} · {p['toolchain']}", '',
            p['summary'][lang], '',
            '<p align="center">', f'  <a href="{escape(target, quote=True)}">',
            f'    <img src="{escape(preview["path"], quote=True)}" width="{preview["width"]}" alt="{escape(preview["alt"][lang], quote=True)}">',
            '  </a>', '</p>', '']
        if 'motion' in preview:
            lines += [f'[{"Посмотреть исходную анимацию" if ru else "Watch the original animation"}]({preview["motion"]})', '']
        lines += [f'**{"Когда достаточно более простого решения" if ru else "When a simpler solution is enough"}:** {p["unnecessary"][lang]}', '']
        lines += ['- ' + c['text'][lang] for c in p['claims']]
        lines += ['', '**Ограничения:**' if ru else '**Limits:**', '']
        lines += ['- ' + c['text'][lang] for c in p['limits']]
        v = p['verification']
        lines += ['', f'**Verified scope · {v["type"]} · {v["date"]}:** {v["scope"][lang]}', '',
            f'[{"Репозиторий" if ru else "Repository"}]({p["url"]}) · '
            f'[Release {release["tag"]}]({p["url"]}/releases/tag/{release["tag"]}) · '
            f'[{"Документация версии" if ru else "Versioned docs"}]({p["url"]}/tree/{release["commit"]}/Docs) · '
            f'[{"Доказательства и область проверки" if ru else "Evidence and scope"}](Docs/Catalog-evidence.md#{p["slug"]})', '', '---', '']
    return '\n'.join(lines + [END])


def evidence_document(data):
    lines = ['# Catalog evidence', '',
        f"Release metadata and source reviewed on **{data['checked_on']}**. Dates use Asia/Almaty.", '',
        'The public release, the versioned source, the linked upstream CI, and independent runtime acceptance are separate facts. A source review establishes what the source declares; a CI success establishes only the workflow scope. No device, pilot, production, or independent Gatekeeper check is claimed by this catalog.', '',
        '| Product | Release | Immutable source | Review type |',
        '| --- | --- | --- | --- |']
    for p in data['products']:
        r = p['release']
        lines.append(f"| [{p['name']}](#{p['slug']}) | [{r['tag']}]({p['url']}/releases/tag/{r['tag']}) | [{r['commit'][:12]}]({p['url']}/tree/{r['commit']}) | {p['verification']['type']} |")
    for p in data['products']:
        lines += ['', f'<a name="{p["slug"]}"></a>', '', f'## {p["name"]}', '',
            f"- **Tag / SHA:** `{p['release']['tag']}` / `{p['release']['commit']}`.",
            f"- **Minimum OS:** {p['minimum_os']}.", f"- **Toolchain:** {p['toolchain']}.",
            '- **Declared third-party Swift dependencies:** ' + (', '.join(p['dependencies']) or 'none in the reusable package manifest') + '.',
            '', '| Claim or limitation | Evidence | Verification type / date |', '| --- | --- | --- |']
        by_id = {e['id']:e for e in p['evidence']}
        for c in p['claims'] + p['limits']:
            refs = [by_id[i] for i in c['evidence']]
            links = '; '.join(f"[{e['id']}]({e['sources'][0]})" for e in refs)
            types = ', '.join(sorted({e['type'] for e in refs}))
            lines.append(f"| {c['text']['en'].replace('|', '/')} | {links} | {types} / {p['verification']['date']} |")
        lines += ['', '### Sources', '']
        for e in p['evidence']:
            links = ' · '.join(f'[source {i+1}]({u})' for i,u in enumerate(e['sources']))
            lines.append(f"- **{e['id']}** · {e['type']} · {e['date']}: {links}")
            if 'sha256' in e:
                lines.append(f"  Archive SHA-256: `{e['sha256']}`.")
        lines += ['', f"- **Preview provenance:** [existing catalog asset]({p['preview']['source']})." + (f" Lossless frame `{p['preview']['frame']}`; original animation remains linked." if 'frame' in p['preview'] else ''),
            '- **Preview scope:** appearance only. The ResizeLint SVG is a terminal illustration, not execution evidence.' if p['kind']=='tool' else '- **Preview scope:** an existing demo capture; appearance alone does not prove a complete workflow.']
    lines += ['', '## ResizeLint distribution boundary', '',
        'The published 1.0.0 Linux archive was re-downloaded and matched SHA-256 `4d1a116520e901076920262f7059a737d4af538738cdae4f8e1ff29df4a24225`. ELF inspection identifies Swift shared-library dependencies including `libswiftCore.so`. A bare Ubuntu version is therefore insufficient. This catalog update does not execute the ELF on Linux; the earlier runtime audit reported exit 127 without Swift libraries.', '',
        'The macOS release workflow includes signing, notarization, stapling, signature checks, and Gatekeeper assessment. The linked successful release run is **upstream CI evidence**. Downloaded macOS artifacts have not received an independent Gatekeeper assessment in this catalog update.', '',
        'Unreleased upstream branches and local release candidates are not substitutes for published versions. Re-check these limitations when selecting a later release.', '']
    return '\n'.join(lines)

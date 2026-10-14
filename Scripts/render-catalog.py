#!/usr/bin/env python3
"""Update manifest-owned README regions and the evidence reference."""
import json
from pathlib import Path
from catalog_content import BEGIN, END, LANGUAGES, catalog_section, evidence_document

ROOT = Path(__file__).resolve().parents[1]

def main():
    data = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    for lang, name in LANGUAGES.items():
        path = ROOT / name
        text = path.read_text(encoding='utf-8')
        if text.count(BEGIN) != 1 or text.count(END) != 1:
            raise SystemExit(f'{name}: expected exactly one catalog:begin/end region')
        start, end = text.index(BEGIN), text.index(END) + len(END)
        path.write_text(text[:start] + catalog_section(data,lang) + text[end:], encoding='utf-8')
    path = ROOT / 'Docs/Catalog-evidence.md'
    path.parent.mkdir(exist_ok=True)
    path.write_text(evidence_document(data), encoding='utf-8')
    print('Updated README.md, README.ru.md and Docs/Catalog-evidence.md from catalog.json')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Guard the independent public case study against private-source additions.
from pathlib import Path
import re
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
required=['README.md','case-study.md','NOTICE.md','SECURITY.md','.osystic/repository.yml',
          'docs/disclosure-boundary.md','docs/validation-evidence.md']
for name in required:
    assert (root/name).is_file(), f'Missing case-study artifact: {name}'
files=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts]
disallowed={'.php','.sql','.zip','.m4v','.mp4','.jpeg','.jpg','.png','.pem','.p12','.db','.sqlite'}
private_markers=['shom'+'oukh','sae'+'.edu.sa','u417'+'552230','cms'+'_private',
                 'BEGIN PRI'+'VATE KEY','ghp_'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
errors=[]
for p in files:
    if p.suffix.lower() in disallowed:errors.append('Disallowed file type: '+str(p.relative_to(root)))
    try:data=p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append('Binary content: '+str(p.relative_to(root)));continue
    for marker in private_markers:
        if marker.lower() in data.lower():errors.append('Private disclosure marker in '+str(p.relative_to(root)))
    if re.search(r'(?i)(?:DB_PASSWORD|API_KEY|ACCESS_TOKEN)\s*=\s*\S{8,}',data):
        errors.append('Secret assignment in '+str(p.relative_to(root)))
# Editorial SVG assets must be safe, self-contained and never masquerade as client screenshots.
for svg in (root/'assets').glob('*.svg'):
    try:
        tree=ET.parse(svg)
        markup=svg.read_text(encoding='utf-8')
        for node in tree.iter():
            tag=node.tag.rsplit('}',1)[-1].lower()
            if tag in {'script','foreignobject','iframe','image'}:
                errors.append(f'Unsafe embedded SVG element {tag}: {svg.relative_to(root)}')
            for attr,value in node.attrib.items():
                name=attr.rsplit('}',1)[-1].lower()
                if name.startswith('on') or name=='href' or 'javascript:' in value.lower():
                    errors.append(f'Unsafe SVG attribute {name}: {svg.relative_to(root)}')
        if 'concept' not in markup.lower() or 'not a screenshot' not in markup.lower():
            errors.append('SVG concept art must explicitly identify its illustrative status: '+str(svg.relative_to(root)))
    except (ET.ParseError, UnicodeDecodeError) as exc:
        errors.append(f'Invalid editorial SVG {svg.relative_to(root)}: {exc}')
for e in errors:print('FAIL:',e)
if errors:raise SystemExit(1)
print('PUBLIC_BOUNDARY_PASS='+str(len(files))+' files; no confidential source, client references or secret patterns')

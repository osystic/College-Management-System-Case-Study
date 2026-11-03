#!/usr/bin/env python3
# Guard the independent public case study against private-source additions.
from pathlib import Path
import re
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
for e in errors:print('FAIL:',e)
if errors:raise SystemExit(1)
print('PUBLIC_BOUNDARY_PASS='+str(len(files))+' files; no confidential source, client references or secret patterns')

"""Read-only #33 predecessor proof and copied-fixture negative gate audit."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
from history_bindings import validate_history
from feet_review import validate_feet_delivery
from face_review import validate_delivery
from beak_review import validate_beak_delivery

BASE='84bee42'
digest=lambda b: hashlib.sha256(b).hexdigest()
git_bytes=lambda path: subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
manifest=json.loads((ROOT/'validation/history/pre_feet_v01/manifest.json').read_bytes())
out={'baseline_commit':subprocess.check_output(['git','rev-parse',BASE],cwd=ROOT,text=True).strip(),
     'review_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
     'history_validator':validate_history(ROOT),'sources':{},'metadata':{},'unchanged_artifacts':{},'negative_probes':{}}
for old,item in manifest['source_relocations'].items():
    actual=(ROOT/item['path']).read_bytes()
    before=git_bytes(old)
    out['sources'][old]={'archive':item['path'],'predecessor_sha256':digest(before),
                         'archive_sha256':digest(actual),'byte_exact':before==actual}

def differences(old,new,path=''):
    if isinstance(old,dict) and isinstance(new,dict):
        for k in old.keys()|new.keys():
            if k not in old or k not in new: yield [path+'/'+k,old.get(k),new.get(k)]
            else: yield from differences(old[k],new[k],path+'/'+k)
    elif isinstance(old,list) and isinstance(new,list):
        if len(old)!=len(new): yield [path+'/length',len(old),len(new)]
        for i,(a,b) in enumerate(zip(old,new)):yield from differences(a,b,path+'/'+str(i))
    elif old!=new: yield [path,old,new]

for old,item in manifest['metadata_relocations'].items():
    before=git_bytes(old)
    snapshot=(ROOT/item['snapshot']).read_bytes()
    current=(ROOT/old).read_bytes()
    out['metadata'][old]={'snapshot_byte_exact':before==snapshot,'git_before_sha256':digest(before),
                         'current_sha256':digest(current),
                         'changes':list(differences(json.loads(before),json.loads(current)))}

paths=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'blender/scene','validation/reviews','design','references'],cwd=ROOT,text=True).splitlines()
for path in paths:
    if path in manifest['metadata_relocations']:continue
    current=ROOT/path
    if not current.exists(): out['unchanged_artifacts'][path]={'missing':True};continue
    before=git_bytes(path)
    actual=current.read_bytes()
    if before.startswith(b'version https://git-lfs.github.com/spec/v1\n'):
        text=before.decode()
        oid=next(line.split(':')[1] for line in text.splitlines() if line.startswith('oid sha256:'))
        size=int(next(line.split()[1] for line in text.splitlines() if line.startswith('size ')))
        out['unchanged_artifacts'][path]={'predecessor_lfs_oid':oid,'actual_sha256':digest(actual),
                                       'bytes':len(actual),'unchanged':digest(actual)==oid and len(actual)==size}
    else:out['unchanged_artifacts'][path]={'bytes':len(actual),'unchanged':before==actual}

with tempfile.TemporaryDirectory(prefix='history-audit-',dir=ROOT/'tmp') as scratch_name:
    scratch=Path(scratch_name)
    for path in ['validation/history/pre_feet_v01/manifest.json']+[v['path'] for v in manifest['source_relocations'].values()]+[v['snapshot'] for v in manifest['metadata_relocations'].values()]+list(manifest['metadata_relocations']):
        target=scratch/path
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/path,target)
    def probe(name,apply,restore):
        apply()
        try: result={'errors':validate_history(scratch)}
        except Exception as e:result={'exception':type(e).__name__,'message':str(e)}
        out['negative_probes'][name]=result
        restore()
    source=scratch/'scripts/legacy/project.py'
    source_bytes=source.read_bytes()
    probe('stale_archived_source',lambda:source.write_bytes(source_bytes+b'# changed\n'),lambda:source.write_bytes(source_bytes))
    target=scratch/'design/silhouette_freeze.json'
    target_bytes=target.read_bytes()
    edited=json.loads(target_bytes)
    edited['checks'][0]['reason']='Changed historical visual decision'
    probe('changed_historical_decision',lambda:target.write_text(json.dumps(edited),encoding='utf-8'),lambda:target.write_bytes(target_bytes))
    snapshot=scratch/manifest['metadata_relocations']['design/silhouette_freeze.json']['snapshot']
    snapshot_bytes=snapshot.read_bytes()
    probe('missing_historical_snapshot',lambda:snapshot.unlink(),lambda:snapshot.write_bytes(snapshot_bytes))
    manifest_path=scratch/'validation/history/pre_feet_v01/manifest.json'
    manifest_bytes=manifest_path.read_bytes()
    amputated=copy.deepcopy(manifest)
    del amputated['source_relocations']['scripts/project.py']
    def omit_source():
        source.write_bytes(source_bytes+b'# changed\n')
        manifest_path.write_text(json.dumps(amputated),encoding='utf-8')
    def restore_source():
        source.write_bytes(source_bytes)
        manifest_path.write_bytes(manifest_bytes)
    probe('removed_manifest_source_plus_changed_archive',omit_source,restore_source)
    amputated=copy.deepcopy(manifest)
    del amputated['metadata_relocations']['design/silhouette_freeze.json']
    def omit_metadata():
        target.write_text(json.dumps(edited),encoding='utf-8')
        manifest_path.write_text(json.dumps(amputated),encoding='utf-8')
    def restore_metadata():
        target.write_bytes(target_bytes)
        manifest_path.write_bytes(manifest_bytes)
    probe('removed_manifest_metadata_plus_changed_decision',omit_metadata,restore_metadata)
    def empty_manifest():
        target.write_text(json.dumps(edited),encoding='utf-8')
        source.write_bytes(source_bytes+b'# changed\n')
        manifest_path.write_text(json.dumps({'source_relocations':{},'metadata_relocations':{}}),encoding='utf-8')
    def restore_all():
        target.write_bytes(target_bytes)
        source.write_bytes(source_bytes)
        manifest_path.write_bytes(manifest_bytes)
    probe('empty_manifest_plus_changed_archive_and_decision',empty_manifest,restore_all)

out['delivery_probes']={}
for name,validator in [('feet_v01',validate_feet_delivery),('beak_v01',validate_beak_delivery),('face_v01',validate_delivery)]:
    folder=ROOT/'validation/reviews'/name
    proof=json.loads((folder/'verification.json').read_bytes())
    decision=json.loads((folder/'review.json').read_bytes())
    def check(proof,decision):
        if name=='face_v01':return validator(ROOT,decision,proof)
        return validator(ROOT,proof,decision)
    result={'baseline':check(proof,decision)}
    changed=copy.deepcopy(proof)
    changed['reference_sha256']={}
    result['omitted_all_reference_bindings']=check(changed,decision)
    changed=copy.deepcopy(proof)
    changed['source_sha256']={}
    result['omitted_all_source_bindings']=check(changed,decision)
    changed=copy.deepcopy(proof)
    changed['reloaded']={}
    result['omitted_all_reload_comparisons']=check(changed,decision)
    out['delivery_probes'][name]=result

(ROOT/'tmp/history-audit-evidence.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'sources':out['sources'],'snapshot_count':len(out['metadata']),
                  'snapshots_byte_exact':all(v['snapshot_byte_exact'] for v in out['metadata'].values()),
                  'unchanged_artifact_count':len(out['unchanged_artifacts']),
                  'artifact_failures':{p:v for p,v in out['unchanged_artifacts'].items() if not v.get('unchanged')},
                  'negative_probes':out['negative_probes'],'delivery_probes':out['delivery_probes']},indent=2))

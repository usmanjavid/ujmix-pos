"""Publish only an explicitly authorized, verified customer installer; never application source or owner material."""
from pathlib import Path
import hashlib,json,os,re,shutil,subprocess,urllib.parse,urllib.request,zipfile
inputs=json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())['inputs'];url=inputs['artifact_url']
parsed=urllib.parse.urlparse(url)
assert parsed.scheme=='https' and parsed.hostname and (parsed.hostname.endswith('.blob.core.windows.net') or parsed.hostname.endswith('.actions.githubusercontent.com') or parsed.hostname.endswith('.vsblob.vsassets.io')),'Unexpected artifact download host'
print('::add-mask::'+url,flush=True)
assert re.fullmatch('[0-9a-f]{40}',inputs['source_commit']) and inputs['source_run'].isdigit()
repo=os.environ['GITHUB_REPOSITORY'];assert repo=='usmanjavid/ujmix-pos'
def command(args):return subprocess.check_output(args,text=True).strip()
assert not json.loads(command(['gh','api',f'repos/{repo}']))['private']
archive=Path('customer-build.zip')
try:
 with urllib.request.urlopen(url,timeout=120) as response,archive.open('wb') as output:shutil.copyfileobj(response,output,1024*1024)
except Exception:
 raise SystemExit('Customer artifact download failed. Obtain a fresh verified artifact URL and retry.')
stage=Path('customer-upload');stage.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 names=z.namelist();assert not any('keygen' in n.lower() or 'issuer' in n.lower() or n.lower().endswith(('.pfx','.pem','.db','.py','.rs','.tsx','.ts')) or 'source.zip' in n.lower() for n in names),'Owner files or application source in customer artifact'
 manifests=[n for n in names if Path(n).name=='customer-manifest.json'];assert len(manifests)==1
 manifest=json.loads(z.read(manifests[0]).decode('utf-8-sig'))
 assert manifest['product']=='UJMix POS' and manifest['windows_verified'] is True
 assert manifest['source_commit']==inputs['source_commit'] and str(manifest['source_run'])==inputs['source_run']
 version=manifest['version'];assert re.fullmatch(r'\d+\.\d+\.\d+',version)
 candidates=[n for n in names if n.endswith('-setup.exe')];assert len(candidates)==1
 installer=stage/f'UJMix-POS-{version}-x64-setup.exe'
 with z.open(candidates[0]) as source,installer.open('wb') as target:shutil.copyfileobj(source,target,1024*1024)
 for name in ['installer-check.json','protection-report.json']:
  matching=[n for n in names if Path(n).name==name];assert len(matching)==1;(stage/name).write_bytes(z.read(matching[0]))
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
assert installer.stat().st_size==manifest['installer_bytes'] and digest(installer)==manifest['installer_sha256'],'Installer does not match verified Windows build'
for name in ['LICENSE','LICENSES.md']:shutil.copy2(name,stage/name)
for p in Path('docs').glob('*'):
 if p.is_file():shutil.copy2(p,stage/p.name)
(stage/'release-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(stage/'SHA256SUMS.txt').write_text(''.join(f'{digest(p)}  {p.name}\n' for p in sorted(stage.iterdir())if p.name!='SHA256SUMS.txt'))
notes=Path('release-notes.md');notes.write_text(f'''UJMix POS {version} for Windows 10/11 x64.\n\nDownload **{installer.name}**. Setup offers with or without optional local AI. No developer tools are required on the customer PC.\n\nSeven-day full trial, new blue branding, adjustable text size, four-hour default idle timeout, secure Remember me, three store phone fields and owner-editable receipt presentation. New invoice numbers start with the store name; saved invoice identities remain unchanged. Software-provider details remain separate at the bottom.\n\nDemo: username **demo**, password **demo123456**. After the trial, activate a 3-month, 6-month, 1-year, 3-year or lifetime license. Earlier UJ Retail customers should contact support for a replacement license before upgrading. Existing store-data identity is preserved. Close the old app and make a tested backup first.\n\nWindows build, archive validation and installed automated diagnostics passed. Physical shop devices and local tax requirements should be checked during your demo.\n\nWebsite: https://www.ujmix.com/ujmix-pos/ · WhatsApp: https://wa.me/923156843398 · Email: usmanjavid@gmail.com\n\nVerify SHA256SUMS.txt. Customer downloads contain no owner tools, issuer keys or application source.\n''')
tag='v'+version
existing=subprocess.run(['gh','release','view',tag,'--repo',repo,'--json','isDraft'],capture_output=True,text=True)
if existing.returncode==0:
 assert json.loads(existing.stdout)['isDraft'],'Published versions are immutable'
 subprocess.run(['gh','release','edit',tag,'--repo',repo,'--title',f'UJMix POS {version} — Windows x64','--notes-file',str(notes),'--prerelease'],check=True)
else:subprocess.run(['gh','release','create',tag,'--repo',repo,'--title',f'UJMix POS {version} — Windows x64','--notes-file',str(notes),'--draft','--prerelease'],check=True)
subprocess.run(['gh','release','upload',tag,'--repo',repo,'--clobber',*[str(p) for p in sorted(stage.iterdir())]],check=True)
release=json.loads(command(['gh','api',f'repos/{repo}/releases/tags/{tag}']));remote={a['name']:a for a in release['assets']}
for p in stage.iterdir():
 item=remote[p.name];assert item['state']=='uploaded' and item['size']==p.stat().st_size
 if item.get('digest'):assert item['digest']=='sha256:'+digest(p)
subprocess.run(['gh','release','edit',tag,'--repo',repo,'--draft=false','--prerelease'],check=True)
print(f'https://github.com/{repo}/releases/tag/{tag}')

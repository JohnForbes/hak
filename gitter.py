from os.path import exists
from subprocess import run as sprun

from hak.one.file.load import f as load
from hak.one.file.save import f as save
from hak.one.string.colour.bright.cyan import f as cy
from hak.one.string.colour.bright.magenta import f as mag

f_M = lambda x: f_X(x, 'Updated', ask=True)
f_A = lambda x: f_X(x, 'Added', ask=True)
f_D = lambda x: f_X(x, 'Removed', ask=False)

def f_X(a, b, ask=True):
  if exists(a):
    print(f'a: {mag(a)}')
    if not any([a.endswith(_) for _ in [
      '.pdf',
      '.bak',
      '.db',
      '.x',
      '.xlsx',
      '.zip',
      '.pkl'
    ]]):
      save(a, load(a))
    sprun(args=['code', a])
  __=mag(a)
  response=input(cy(f"Proceed with '")+a+cy(f"'? (Q/Y/N):")) if ask else 'Y'
  # response = 'Y'
  if response=='Y':
    result = sprun(args=['git', 'add', a], capture_output=True, cwd='.')
    print(cy("Executing 'git add'"))
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git commit'"))
    result = sprun(
      args=['git', 'commit', '-m', f'{b} {a}.'], capture_output=True, cwd='.'
    )
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git push'"))
    result = sprun(args=['git', 'push'], capture_output=True, cwd='.')
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
  elif response=='Q': exit()
  else: print('Cancelled.')

def main():
  print(cy("Executing 'git pull'"))
  result = sprun(args=['git', 'pull'], capture_output=True, cwd='.')
  print(cy('result.stdout.decode():')+f' {result.stdout.decode()}')
  print(cy("Executing 'git status -s'"))
  result = sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')
  q_0=[_ for _ in result.stdout.decode().split("\n") if _]
  result = sprun(
    args=['git', 'ls-files', '--others', '--exclude-standard'],
    capture_output=True,
    cwd='.'
  )
  q_1=[f'?? {_}' for _ in result.stdout.decode().split("\n") if _]
  q = [_ for _ in (q_0+q_1) if not _.endswith('/')]
  d={}
  for j in q:
    z=3
    k, v=j[:z-1], j[z:]
    if k not in d: d[k]=set()
    d[k].add(v)
  __={'??': 'Added', ' D': 'Removed', ' M': 'Updated'}
  if ' M' in d: _=sorted(d[' M'])[0]; f_M(_)
  if '??' in d: _=sorted(d['??'])[0]; f_A(_)
  if ' D' in d: _=sorted(d[' D'])[0]; f_D(_)
  if any([_ in d for _ in [' M', '??', ' D']]): main()

if __name__=='__main__': main()

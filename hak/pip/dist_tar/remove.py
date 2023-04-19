from os.path import exists

from hak.directory.make import f as mkdir
from hak.directory.empty import f as empty_directory
from hak.directory.remove import f as rmdirie
from hak.file.save import f as save
from hak.string.print_and_return_false import f as pf

f = lambda x='.': empty_directory(x)
temp_root = './_dist_tars_remove'
# target = f'{temp_root}/dist'

def up():
  mkdir(temp_root)
  print(temp_root)
  # print(target)
  _ = f'{temp_root}/junk.tar'
  save(_, 'junk')
  return _

def dn(): rmdirie(temp_root)

def t():
  _ = up()
  f(temp_root)
  if not exists(_): return pf(f'not exists({_})')
  dn()
  if exists(temp_root): return pf(f'exists({temp_root})')
  return True

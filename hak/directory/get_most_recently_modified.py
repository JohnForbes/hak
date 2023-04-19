from hak.directory.make import f as mkdir
from hak.file.save import f as save
from hak.directory.remove import f as rmdir
from hak.string.print_and_return_false import f as pf
from os.path import getmtime
from hak.list.strings.filepaths.get import f as get_filepaths

def f(x):
  filepaths = get_filepaths(x, [])
  newest = {'name': '', 'time': float('inf')}
  for filename in filepaths:
    last_modified_time = getmtime(filename)
    if last_modified_time < newest['time']:
      newest = {'file': filename, 'time': last_modified_time}
  return newest['file']

def up():
  x = {}
  x['dir_name'] = './test_directory_get_most_recently_modified'
  
  # Create test directory
  mkdir(x['dir_name'])

  # create old file
  x['old_file_content'] = 'ABC'
  x['old_file_path'] = f"{x['dir_name']}/old_file.txt"
  save(x['old_file_path'], x['old_file_content'])

  # create new file
  x['new_file_content'] = 'XYZ'
  x['new_file_path'] = f"{x['dir_name']}/new_file.txt"
  save(x['new_file_path'], x['new_file_content'])

  return x

dn = lambda x: rmdir(x['dir_name'])

def t():
  x = up()
  y = x['old_file_path']
  z = f(x['dir_name'])
  dn(x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])
from hak.one.function.function import Function
from hak.one.file.save import f as save
from hak.one.file.remove import f as remove
from hak.one.file.load import f as load

f = lambda fn, root='.': save(f'{root}/_{fn.name}.py', fn.text)
_filepath = './_foo.py'
dn = lambda: remove(_filepath)

def t():
  fn = Function('foo', 'f = lambda: "foo"\t = lambda: "foo" == f()')
  f(fn)
  result = load(_filepath) == fn.text
  dn()
  return result

from hak.pxyz import f as pxyz

f = lambda obj, keys: {k: obj[k] for k in [k for k in keys if k in obj]}

def t():
  x = {
    'obj': {'a': 'AAA', 'b': 'BBB', 'c': "CCC", 'd': "DDD"},
    'keys': ['a', 'c', 'e']
  }
  y = {'a': 'AAA', 'c': "CCC"}
  z = f(**x)
  return pxyz(x, y, z)

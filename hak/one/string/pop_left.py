from hak.pxyz import f as pxyz

def f(x): return (x[1:], x[:1])

def t():
  x = 'abcd'
  y = ('bcd', 'a')
  z = f(x)
  return pxyz(x, y, z)

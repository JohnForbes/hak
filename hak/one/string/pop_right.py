from hak.pf import f as pf

def f(x): return (x[:len(x)-1], x[len(x)-1:])

def t():
  x = 'abc'
  y = ('ab', 'c')
  z = f(x)
  return y == z or pf(['y != z', f'x: {x}', f'y: {y}', f'z: {z}'])

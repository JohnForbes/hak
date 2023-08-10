from hak.pf import f as pf

def f(x, y, z):
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

t = lambda: True

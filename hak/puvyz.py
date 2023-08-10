from hak.pf import f as pf

def f(u, v, y, z):
  return y == z or pf([f'u: {u}', f'v: {v}', f'y: {y}', f'z: {z}'])

t = lambda: True

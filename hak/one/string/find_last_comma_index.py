from hak.pf import f as pf
from hak.one.string.find_last_char import f as find_last_char

f = lambda x: find_last_char(x, ',')

def t():
  x = 'a,b,c,de'
  y = 5
  z = f(x)
  return y == z or pf(['y != z', f'x: {x}', f'y: {y}', f'z: {z}'])

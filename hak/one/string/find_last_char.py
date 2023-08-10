from hak.pf import f as pf

f = lambda string, char: len(string)-string[::-1].find(char)-1

def t():
  x = {'string': 'a,b,c,de', 'char': ','}
  y = 5
  z = f(**x)
  return y == z or pf(['y != z', f'x: {x}', f'y: {y}', f'z: {z}'])

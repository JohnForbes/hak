from hak.one.number.float.epsilon import ε
from hak.one.string.print_and_return_false import f as pf

# src.float.snap_to_zero
f = lambda x: 0 if abs(x) < 1e-10 else x

def t_zero():
  x = 0
  y = 0
  z = f(x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t_one():
  x = 1
  y = 1
  z = f(x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t_negative_epsilon():
  x = -ε
  y = 0
  z = f(x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t_positive_epsilon():
  x = ε
  y = 0
  z = f(x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t():
  if not t_zero(): return pf('t_zero failed')
  if not t_one(): return pf('t_one failed')
  if not t_negative_epsilon(): return pf('t_negative_epsilon failed')
  if not t_positive_epsilon(): return pf('t_positive_epsilon failed')
  return True

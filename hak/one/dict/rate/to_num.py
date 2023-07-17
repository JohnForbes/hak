from hak.one.string.print_and_return_false import f as pf
from hak.one.dict.rate.make import f as make_rate
from hak.pxyz import f as pxyz

def f(x):
  if x['denominator'] == 0: raise ZeroDivisionError('denominator must not be 0')
  if x['denominator'] == 1: return round(x['numerator'])
  return x['numerator']/x['denominator']

def t_int():
  x = make_rate(2, 1, {'int': 1})
  y = type(2)
  z = type(f(x))
  return pxyz(x, y, z)

def t_float():
  x = make_rate(1, 2, {'float': 1})
  y = type(0.5)
  z = type(f(x))
  return pxyz(x, y, z)

def t():
  if not t_int(): return pf('!t_int')
  if not t_float(): return pf('!t_float')
  return True

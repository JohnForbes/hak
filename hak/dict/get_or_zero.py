from hak.dict.get_or_default import f as get_or_default
from hak.string.print_and_return_false import f as pf

# get_value_by_key_or_zero
# f_v_if_k_else_0
f = lambda d, k: get_or_default(d, k, 0)

def t_successful_retrieval():
  x = {'d': {'a': 1}, 'k': 'a'}
  y = x['d'][x['k']]
  z = f(**x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t_default_to_zero():
  x = {'d': {'a': 1}, 'k': 'b'}
  y = 0
  z = f(**x)
  return y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'])

def t():
  if not t_successful_retrieval(): return pf('!t_successful_retrieval')
  if not t_default_to_zero(): return pf('!t_default_to_zero')
  return True
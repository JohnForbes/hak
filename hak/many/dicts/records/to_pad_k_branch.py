# ignore_overlength_lines
from .k_branch_and_k_leaf.to_leaf_col_width import f as records_k_branch_k_leaf_to_leaf_col_width
from .k_branch.to_sorted_leaf_keys import f as records_k_branch_to_sorted_leaf_keys
from hak.cell_val_widths_to_aggregate_width import f as cell_val_widths_to_aggregate_width
from hak.one.string.print_and_return_false import f as pf
from hak.pxyz import f as pxyz

# f_q
# records_to_pad_k_branch
def f(records, k_branch):
  w = cell_val_widths_to_aggregate_width([
    records_k_branch_k_leaf_to_leaf_col_width(records, k_branch, k)
    for k
    in records_k_branch_to_sorted_leaf_keys(records, k_branch)
  ])
  return f'{k_branch:>{w}}'

from hak.one.dict.rate.make import f as make_rate
_records = [
  {
    'prices': {
      'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': make_rate(1, 1, {'apple': 1}),
      'bananazzz': make_rate(2, 1, {'banana': 1}),
      'pearzzzzzz': make_rate(3, 1, {'pear': 1})
    },
    'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
  }, 
  {
    'prices': {
      'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': make_rate(4, 1, {'apple': 1}),
      'bananazzz': make_rate(5, 1, {'banana': 1}),
      'pearzzzzzz': make_rate(6, 1, {'pear': 1})
    },
    'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
  }
]

def t_prices():
  x = {'records': _records, 'k_branch': 'prices'}
  y = '            prices'
  z = f(**x)
  return pxyz(x, y, z)

def t_volumes():
  x = {'records': _records, 'k_branch': 'volumes'}
  y = '                          volumes'
  z = f(**x)
  return pxyz(x, y, z)

def t_zloops():
  x = {'records': _records, 'k_branch': 'zloops'}
  y = 'zloops'
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return True

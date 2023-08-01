from hak.get_col_w_fr_k_branch_k_leaf import f as get_col_w_fr_k_branch_k_leaf
from hak.one.string.print_and_return_false import f as pf
from hak.pxyz import f as pxyz

# f_pad_subkey
f = lambda records, k_branch, k_leaf: (
  f'{k_leaf:>{get_col_w_fr_k_branch_k_leaf(records, k_branch, k_leaf)}}'
)

def t():
  if not t_prices_apples():      return pf('!t_prices_apples')
  if not t_prices_bananas():     return pf('!t_prices_bananas')
  if not t_volumes_applezzz():   return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz():  return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop():       return pf('!t_zloops_zloop')
  return True

_records = [
  {
    'prices': {
      'apples': {
        'numerator': 1,
        'denominator': 4,
        'unit': {'$': 1, 'apple': -1}
      },
      'bananas': {
        'numerator': 1,
        'denominator': 2,
        'unit': {'$': 1, 'banana': -1}
      }
    },
    'volumes': {
      'applezzz': {'numerator': 1, 'denominator': 1, 'unit': {'apple': 1}},
      'bananazzz': {'numerator': 2, 'denominator': 1, 'unit': {'banana': 1}},
      'pearzzzzzz': {'numerator': 3, 'denominator': 1, 'unit': {'pear': 1}}
    },
    'zloops': {
      'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}
    }
  },
  {
    'prices': {
      'apples': {
        'numerator': 3,
        'denominator': 4,
        'unit': {'$': 1, 'apple': -1}
      },
      'bananas': {
        'numerator': 1,
        'denominator': 1,
        'unit': {'$': 1, 'banana': -1}
      }
    },
    'volumes': {
      'applezzz': {'numerator': 4, 'denominator': 1, 'unit': {'apple': 1}},
      'bananazzz': {'numerator': 5, 'denominator': 1, 'unit': {'banana': 1}},
      'pearzzzzzz': {'numerator': 6, 'denominator': 1, 'unit': {'pear': 1}}
    },
    'zloops': {
      'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}
    }
  }
]

def t_prices_apples():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'apples'}
  y = ' apples'
  z = f(**x)
  return pxyz(x, y, z)

def t_prices_bananas():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'bananas'}
  y = ' bananas'
  z = f(**x)
  return pxyz(x, y, z)

def t_volumes_applezzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'applezzz'}
  y = 'applezzz'
  z = f(**x)
  return pxyz(x, y, z)

def t_volumes_bananazzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'bananazzz'}
  y = 'bananazzz'
  z = f(**x)
  return pxyz(x, y, z)

def t_volumes_pearzzzzzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'pearzzzzzz'}
  y = 'pearzzzzzz'
  z = f(**x)
  return pxyz(x, y, z)

def t_zloops_zloop():
  x = {'records': _records, 'k_branch': 'zloops', 'k_leaf': 'zloop'}
  y = ' zloop'
  z = f(**x)
  return pxyz(x, y, z)

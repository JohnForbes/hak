from hak.pxyz import f as pxyz
from hak.one.dict.get_sorted_keys import f as get_sorted_keys
from hak.one.string.print_and_return_false import f as pf
from hak.one.dict.rate.make import f as make_rate

# records_k_branch_to_sorted_leaf_keys
f = lambda records, field_name: get_sorted_keys(records[0][field_name])

def t_prices():
  x = {
    'records': [
      {
        'prices': {
          'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 2, {'$': 1, 'banana': -1}),
        },
        '...': {}
      },
      {
        'prices': {
          'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 1, {'$': 1, 'banana': -1}),
        },
        '...': {}
      }
    ],
    'field_name': 'prices'
  }
  y = ['apples', 'bananas']
  z = f(**x)
  return pxyz(x, y, z)

def t_volumes():
  x = {
    'records': [
      {
        '...': {},
        'volumes': {
          'applezzz': make_rate(1, 1, {'apple': 1}),
          'bananazzz': make_rate(2, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(3, 1, {'pear': 1})
        },
        '...': {}
      }, 
      {
        '...': {},
        'volumes': {
          'applezzz': make_rate(4, 1, {'apple': 1}),
          'bananazzz': make_rate(5, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(6, 1, {'pear': 1})
        },
        '...': {}
      }
    ],
    'field_name': 'volumes'
  }
  y = ['applezzz', 'bananazzz', 'pearzzzzzz']
  z = f(**x)
  return pxyz(x, y, z)

def t_zloops():
  x = [
    {
      '...': {},
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }, 
    {
      '...': {},
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  a = 'zloops'
  y = ['zloop']
  z = f(x, a)
  return pxyz(x, y, z)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return True

from hak.many.dicts.get_sorted_keys_of_first_dict import f as get_K
from hak.many.dicts.get_top_heading_field_width import f as get_top_head_width
from hak.one.string.print_and_return_false import f as pf
from hak.f_q import f as f_q
from hak.pxyz import f as pxyz

# do_fn_a_on_sorted_keys_of_x
f = lambda x, a: [a(x, k) for k in get_K(x)]

_records = [
  {
    'prices':
    {
      'apples': {
        'numerator': 1, 'denominator': 4, 'unit': {'$': 1, 'apple': -1}
      },
      'bananas': {
        'numerator': 1, 'denominator': 2, 'unit': {'$': 1, 'banana': -1}
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
    'prices':
    {
      'apples': {
        'numerator': 3, 'denominator': 4, 'unit': {'$': 1, 'apple': -1}
      },
      'bananas': {
        'numerator': 1, 'denominator': 1, 'unit': {'$': 1, 'banana': -1}
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

def t_0():
  x = _records
  a = get_top_head_width
  y = [18, 33, 6]
  z = f(x, a)
  return pxyz(x, y, z)

def t_1():
  x = _records
  a = f_q
  y = ['            prices', '                          volumes', 'zloops']
  z = f(x, a)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return True

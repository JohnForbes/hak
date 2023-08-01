from hak.f_o import f as f_o
from hak.f_m import f as f_m
from hak.f_n import f as f_n
from hak.pxyz import f as pxyz

# f_horizontal_line
f = lambda x: f_o([f_m(x, a, b) for (a, b) in f_n(x)])

def t():
  x = [
    {
      'prices': {
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
      'prices': {
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
  y = '|---------|----------|----------|-----------|------------|--------|'
  z = f(x)
  return pxyz(x, y, z)

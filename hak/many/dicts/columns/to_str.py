from datetime import date
from hak.one.dict.column.get_width import f as get_column_width
from hak.one.dict.column.make import f as make_column
from hak.one.dict.column.to_str import f as column_to_str
from hak.one.string.print_and_return_false import f as pf
from hak.pxyz import f as pxyz
from hak.one.list.remove_duplicates import f as remove_duplicates
from hak.many.strings.lines._anon_0 import f as h

def g(x):
  return sum(x) + (len(x)-1)*len('-|-')

def _f_a(columns, separator='|'):
  column_strings = [column_to_str(c) for c in columns]
  return '\n'.join([
    separator.join([
      column_strings[column_index].split('\n')[i]
      for column_index
      in range(len(columns))
    ])
    for i in range(len(column_strings[0].split('\n')))
  ])

def _f_b(columns, separator='|'):
  paths = remove_duplicates(c['path'] for c in columns)
  path_width_lists = {p: [] for p in paths}

  for c in columns:
    p = c['path']
    path_width_lists[p].append(get_column_width(c))
  
  path_widths = {
    p: max(g(path_width_lists[p]), len(p)) for p in path_width_lists
  }

  _rows = _f_a(columns, separator).split('\n')

  path_head_bar = '-'+'-|-'.join([   '-'*path_widths[p]    for p in paths])+'-'
  path_head     = ' '+' | '.join([f'{p:>{path_widths[p]}}' for p in paths])+' '

  return '\n'.join(h([
    path_head_bar,
    path_head,
    *_rows
  ]))


f = lambda columns, separator='|': (
  _f_a if set([c['path'] for c in columns]) == {()} else
  _f_b
)(columns, separator)

def t_0():
  x = {
    'columns': [
      make_column('abc', [0, 1, 2, 3]),
      make_column('ghi', [0, 10, 200, 3000])
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------',
    ' abc |  ghi ',
    '-----|------',
    '   0 |    0 ',
    '   1 |   10 ',
    '   2 |  200 ',
    '   3 | 3000 ',
    '-----|------',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)

def t_1():
  x = {
    'columns': [
      make_column('abc', [0, 1, 2, 3]),
      make_column('ghi', [0, 10, 200, 3000]),
      make_column('jklm', ['abc', 'blergh', 'wragh', 'hmmm'])
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------|--------',
    ' abc |  ghi |   jklm ',
    '-----|------|--------',
    '   0 |    0 |    abc ',
    '   1 |   10 | blergh ',
    '   2 |  200 |  wragh ',
    '   3 | 3000 |   hmmm ',
    '-----|------|--------',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)

def t_date():
  x = {
    'columns': [
      make_column('abc', [0, 1, 2, 3]),
      make_column('ghi', [0, 10, 200, 3000]),
      make_column('jklm', ['abc', 'blergh', 'wragh', 'hmmm']),
      make_column(
        'date',
        [
          date(2023, 1, 1),
          date(2023, 2, 1),
          date(2023, 3, 1),
          date(2023, 4, 1)
        ]
      )

    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------|--------|------------',
    ' abc |  ghi |   jklm |       date ',
    '-----|------|--------|------------',
    '   0 |    0 |    abc | 2023-01-01 ',
    '   1 |   10 | blergh | 2023-02-01 ',
    '   2 |  200 |  wragh | 2023-03-01 ',
    '   3 | 3000 |   hmmm | 2023-04-01 ',
    '-----|------|--------|------------',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)

def t_common_path():
  x = {
    'columns': [
      make_column('abc', [0,  1,   2,    3], 'numbers'),
      make_column('ghi', [0, 10, 200, 3000], 'numbers'),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------',
    '    numbers ',
    '-----|------',
    ' abc |  ghi ',
    '-----|------',
    '   0 |    0 ',
    '   1 |   10 ',
    '   2 |  200 ',
    '   3 | 3000 ',
    '-----|------',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)
  # return pxyz(x, [y], [z])

def t_numbers_let_paths():
  x = {
    'columns': [
      make_column('abc', [0,  1,   2,    3], 'numbers'),
      make_column('ghi', [0, 10, 200, 3000], 'numbers'),
      make_column('jkl', list('abcd'), 'let'),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------|-----',
    '    numbers | let ',
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '   0 |    0 |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)

def t_numbers_letters_paths():
  x = {
    'columns': [
      make_column('abc', [0,  1,   2,    3], 'numbers'),
      make_column('ghi', [0, 10, 200, 3000], 'numbers'),
      make_column('jkl', list('abcd'), 'letters'),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------|---------',
    '    numbers | letters ',
    '-----|------|---------',
    ' abc |  ghi |     jkl ',
    '-----|------|---------',
    '   0 |    0 |       a ',
    '   1 |   10 |       b ',
    '   2 |  200 |       c ',
    '   3 | 3000 |       d ',
    '-----|------|---------',
  ])
  z = f(**x)
  return pxyz(x, '\n'+y, '\n'+z)
  # return pxyz(x, [y], [z])

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_date(): return pf('!t_date')
  if not t_common_path(): return pf('!t_common_path')
  if not t_numbers_let_paths(): return pf('!t_numbers_let_paths')
  if not t_numbers_letters_paths(): return pf('!t_numbers_letters_paths')
  return True

from datetime import date
from hak.one.dict.column.make import f as make_column
from hak.one.dict.column.to_str import f as column_to_str
from hak.one.string.print_and_return_false import f as pf
from hak.pxyz import f as pxyz

def f(columns, separator='|'):
  column_strings = [column_to_str(c) for c in columns]
  rows = '\n'.join([
    separator.join([
      column_strings[column_index].split('\n')[i]
      for column_index
      in range(len(columns))
    ])
    for i in range(len(column_strings[0].split('\n')))
  ])
  return rows

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

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_date(): return pf('!t_date')
  return True

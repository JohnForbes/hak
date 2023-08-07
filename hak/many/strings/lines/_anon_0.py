from hak.pxyz import f as pxyz
from hak.one.string.find_last_char import f as find_last_char

def f(x):
  _lines = []
  top_width = len(x[0])
  for l in x:
    if len(l) < top_width:
      # find last pipe
      j = find_last_char(l, '|')+1
      d = l[0]*(top_width - len(l))
      _l = l[:j]+d+l[j:]
    else:
      _l = l
    _lines.append(_l)

  return _lines

def t():
  x = [
    '------------|---------',
    '    numbers | letters ',
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '   0 |    0 |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----'
  ]
  y = [
    '------------|---------',
    '    numbers | letters ',
    '-----|------|---------',
    ' abc |  ghi |     jkl ',
    '-----|------|---------',
    '   0 |    0 |       a ',
    '   1 |   10 |       b ',
    '   2 |  200 |       c ',
    '   3 | 3000 |       d ',
    '-----|------|---------'
  ]
  z = f(x)
  return pxyz(x, str(y), str(z))

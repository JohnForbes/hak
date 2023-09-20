from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.string.colour.bright.blue import f as bb
from hak.string.colour.bright.cyan import f as bc
from hak.string.colour.bright.green import f as bg
from hak.string.colour.bright.magenta import f as bm
from hak.string.colour.bright.red import f as br
from hak.string.colour.bright.white import f as bw
from hak.string.colour.bright.yellow import f as by
from hak.string.colour.dark.blue import f as db
from hak.string.colour.dark.cyan import f as dc
from hak.string.colour.dark.green import f as dg
from hak.string.colour.dark.magenta import f as dm
from hak.string.colour.dark.red import f as dr
from hak.string.colour.dark.white import f as dw
from hak.string.colour.dark.yellow import f as dy

# src.string.decolour
def f(x):
  for _ in [
    '\x1b[0;0m',
    *[f'\x1b[{_a};3{_b}m' for _b in range(1, 8) for _a in range(0, 2)],
  ]:
    x = x.replace(_, '')
  return x

def t():
  if not pxyf(bb('abc'), 'abc', f, show_as_lists=1): return pf('t_bb failed')
  if not pxyf(bc('abc'), 'abc', f, show_as_lists=1): return pf('t_bc failed')
  if not pxyf(bg('abc'), 'abc', f, show_as_lists=1): return pf('t_bg failed')
  if not pxyf(bm('abc'), 'abc', f, show_as_lists=1): return pf('t_bm failed')
  if not pxyf(br('abc'), 'abc', f, show_as_lists=1): return pf('t_br failed')
  if not pxyf(bw('abc'), 'abc', f, show_as_lists=1): return pf('t_bw failed')
  if not pxyf(by('abc'), 'abc', f, show_as_lists=1): return pf('t_by failed')
  if not pxyf(db('abc'), 'abc', f, show_as_lists=1): return pf('t_db failed')
  if not pxyf(dc('abc'), 'abc', f, show_as_lists=1): return pf('t_dc failed')
  if not pxyf(dg('abc'), 'abc', f, show_as_lists=1): return pf('t_dg failed')
  if not pxyf(dm('abc'), 'abc', f, show_as_lists=1): return pf('t_dm failed')
  if not pxyf(dr('abc'), 'abc', f, show_as_lists=1): return pf('t_dr failed')
  if not pxyf(dw('abc'), 'abc', f, show_as_lists=1): return pf('t_dw failed')
  if not pxyf(dy('abc'), 'abc', f, show_as_lists=1): return pf('t_dy failed')
  return 1

if __name__ == '__main__': print(t())

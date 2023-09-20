# ignore_overlength_lines

from datetime import date

from .financial_year.get_end_date import f as f_fy
from .financial_year.make import f as mkfy
from .month.get_end_date import f as get_col_hor_line_from_records

from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.dict.period.month.make import f as mk_month

# get_ω
f = lambda x: (get_col_hor_line_from_records if 'month' in x else f_fy)(x)

t_fy = lambda: pxyf(
  {'financial_year': mkfy({'start_year': 2022})},
  date(2023, 6, 30),
  f
)

t_0 = lambda: pxyf({'month': mk_month(2016,  5)}, date(2016,  5, 31), f)
t_1 = lambda: pxyf({'month': mk_month(2017,  6)}, date(2017,  6, 30), f)
t_2 = lambda: pxyf({'month': mk_month(2020,  2)}, date(2020,  2, 29), f)
t_3 = lambda: pxyf({'month': mk_month(2021,  2)}, date(2021,  2, 28), f)
t_4 = lambda: pxyf({'month': mk_month(2021, 12)}, date(2021, 12, 31), f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_3(): return pf('!t_3')
  if not t_4(): return pf('!t_4')
  if not t_fy(): return pf('!t_fy')
  return 1

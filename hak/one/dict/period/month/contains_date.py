from datetime import date
from hak.one.dict.period.month.get_start_date import f as get_α_d
from hak.one.dict.period.month.get_end_date import f as get_ω_d
from hak.one.string.print_and_return_false import f as pf

# contains_date
f = lambda x: get_α_d(x['month']) <= x['date'] <= get_ω_d(x['month'])

def t():
  x = {'month': {'year': 2022, 'month_number': 1}, 'date': date(2022, 1, 10)}
  y = True
  z = f(x)
  return y == z or pf(f'expected {x["date"]} to be in {x["month"]}')

from hak.calculate_duration_bar_width import f as get_w
w_max = 23

def f(duration_ms):
  w = get_w(duration_ms)
  return (w*'█' + (w_max-w)*' ', w)

t = lambda: all([
  ('                       ', 0) == f(-1),
  ('                       ', 0) == f(0),
  ('                       ', 0) == f(1),
  ('█                      ', 1) == f(2),
  ('██                     ', 2) == f(4),
  ('███                    ', 3) == f(8), 
  ('████                   ', 4) == f(16), 
  ('█████                  ', 5) == f(32), 
  ('██████                 ', 6) == f(64), 
  ('███████                ', 7) == f(128), 
  ('████████               ', 8) == f(256), 
  ('█████████              ', 9) == f(512), 
  ('██████████             ', 10) == f(1024), 
  ('███████████            ', 11) == f(2048), 
  ('████████████           ', 12) == f(4096), 
  ('█████████████          ', 13) == f(8192), 
  ('██████████████         ', 14) == f(16384), 
  ('███████████████        ', 15) == f(32768), 
  ('████████████████       ', 16) == f(65536), 
  ('█████████████████      ', 17) == f(131072), 
  ('██████████████████     ', 18) == f(262144), 
  ('███████████████████    ', 19) == f(524288), 
  ('████████████████████   ', 20) == f(1048576), 
  ('█████████████████████  ', 21) == f(2097152), 
  ('██████████████████████ ', 22) == f(4194304), 
  ('███████████████████████', 23) == f(8388608), 
  ('███████████████████████', 23) == f(9000000), 
])

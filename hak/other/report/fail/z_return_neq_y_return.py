from hak.one.string.colour.bright.red import f as danger
from hak.one.duration import f as duration
from hak.one.string.colour.primary import f as pri
from hak.one.string.colour.secondary import f as sec
from hak.other.report.summarise_file import f as summarise_file
from time import time

f = lambda name, x_args, y_return, z_return, time_started, max_filename_len: (
  False, '\n'.join([
    '|'.join([
      "\r",
      f"{danger('  FAIL  ')}",
      f" {name:{max_filename_len}} ",
      f" {duration(time_started, name)} ",
      ""
    ]),
    f"{danger('mode:')} {'y_return != z_return'}",
    f"{pri('Input       x_args: ')} {summarise_file(str(x_args))}",
    f"{pri('y y_return: ')} {summarise_file(str(y_return))}",
    f"{pri('z z_return: ')} {summarise_file(str(z_return))}",
  ])
)

def t():
  e_result = False
  e_message_l = '|'.join([
    "\r",
    "\x1b[1;31m  FAIL  \x1b[0;0m",
    " fake_name ",
    " \x1b[1;32m                           "
  ])
  e_message_r = '\n'.join([
    "\x1b[0;0m |",
    "\x1b[1;31mmode:\x1b[0;0m y_return != z_return",
    "\x1b[1;34mInput       x_args: \x1b[0;0m {'a': 0, 'b': 1}",
    "\x1b[1;34my y_return: \x1b[0;0m 0.5",
    "\x1b[1;34mz z_return: \x1b[0;0m 0.5",
  ])

  o_result, o_message = f('fake_name', {'a': 0, 'b': 1}, 0.5, 0.5, time(), 9)

  return all([
    e_result == o_result,
    e_message_l == o_message[:len(e_message_l)],
    e_message_r == o_message[len(o_message) - len(e_message_r):]
  ])

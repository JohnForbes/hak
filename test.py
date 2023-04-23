from hak.test.check_final_line import f as check_final_line
from hak.test.check_line_lengths import f as check_line_lengths
from hak.test.oldest_file.print import f as print_oldest_file
from hak.test.do import f as do_test

if __name__ == '__main__':
  print('|'+'-'*78+'|')
  z = do_test(False)
  print(z['message'])
  if z['result']:
    check_line_lengths()
    check_final_line()
    print_oldest_file()
  print('|'+'-'*78+'|')

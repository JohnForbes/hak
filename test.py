from hak.test.final_line.check import f as check_final_line
from hak.test.line_lengths.check import f as check_line_lengths
from hak.test.oldest_file.print import f as print_oldest_file
from hak.test.do import f as do_test
from hak.directory.clean import f as clean_directory

if __name__ == '__main__':
  print('|'+'-'*78+'|')
  clean_directory('.')
  z = do_test(False)
  print(z['message'])
  if z['result']:
    check_line_lengths()
    check_final_line()
    print_oldest_file()
  print('|'+'-'*78+'|')

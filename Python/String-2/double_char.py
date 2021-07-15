#Given a string, return a string where for every char in the original, there are two chars.


#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  string_emp = ''
  for i in range(0, len(str)):
    string_emp += str[i] * 2
  return string_emp

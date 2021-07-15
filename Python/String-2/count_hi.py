#Return the number of times that the string "hi" appears anywhere in the given string.


#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2

def count_hi(str):
  count = 0
  string_emp = 'hi'
  for i in range(0, len(str)):
    str_hi = str[i:i+2]
    if string_emp == str_hi:
      count += 1
  return count

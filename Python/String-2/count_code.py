#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

def count_code(str):
  count = 0
  index = 0
  x = ["co" + i + "e" for i in str.lower()]
  for i in x:
    if i in str[index:]:
      index = str.find(i) + 1
      count += 1
  return count

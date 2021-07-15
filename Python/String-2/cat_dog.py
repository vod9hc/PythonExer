#Return True if the string "cat" and "dog" appear the same number of times in the given string.


#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True

def cat_dog(str):
  cnt_cat = 0
  cnt_dog = 0
  for i in range(0, len(str)):
    if 'cat' == str[i:i+3]:
      cnt_cat += 1
    if 'dog' == str[i:i+3]:
      cnt_dog += 1
  if cnt_cat == cnt_dog:
    return True
  return False

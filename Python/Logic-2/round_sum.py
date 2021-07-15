#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


#round_sum(16, 17, 18) → 60
#round_sum(12, 13, 14) → 30
#round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
  a = round10(a)
  b = round10(b)
  c = round10(c)
  return a + b + c
  
  
def round10(num):
  val = 0
  val_down = (num // 10) * 10
  val_up = val_down + 10
  if (num - val_down) >= (val_up - num):
    val += val_up
  else:
    val += val_down
  return val

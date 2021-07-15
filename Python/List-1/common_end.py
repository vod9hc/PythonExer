#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


#common_end([1, 2, 3], [7, 3]) → True
#common_end([1, 2, 3], [7, 3, 2]) → False
#common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  if a < 1 or b < 1:
    return False
  first_a = a[0]
  last_a = a[-1]
  first_b  = b[0]
  last_b = b[-1]
  if last_a == last_b or first_a ==  first_b:
    return True
  return False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  array12 = nums
  for i in range(0, len(array12)):
    if array12[i:i+3] == [1, 2, 3]:
      return True
  return False

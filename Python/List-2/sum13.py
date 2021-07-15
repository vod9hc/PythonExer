#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  sumv = 0
  value_near13 = 0
  if len(nums) < 1:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13 and (i + 1) < len(nums):
      value_near13 += nums[i+1]
    if nums[i] != 13:
      sumv += nums[i]
    if value_near13 == 13:
      return 0
  return sumv - value_near13

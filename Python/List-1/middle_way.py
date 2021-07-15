#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


#middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
#middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
#middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  arr_mid = []
  mid_a = a[1]
  mid_b = b[1]
  arr_mid.append(mid_a)
  arr_mid.append(mid_b)
  return arr_mid

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


#make_pi() → [3, 1, 4]

def make_pi():
  pi = str(3.14)
  new_pi = []
  for i in pi:
    if i == '.':
      continue
    else:
      i = int(i)
      new_pi.append(i)
  return new_pi

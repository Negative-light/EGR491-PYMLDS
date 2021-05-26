x = 10
while x > 0:
  if (x % 3) == 0:
     x *= 5
     x -= 7
     continue
  print(x)
  x -= 1
  if x > 100:
     break
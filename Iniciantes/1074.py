A = int(input())
for x in range(1, A+1):
  b = int(input())
  if (b % 2 == 1) and (b > 0):
    print("ODD POSITIVE")
  elif (b % 2 == 0) and (b > 0):
    print("EVEN POSITIVE")

  elif (b % 2 == 1) and (b < 0):
    print("ODD NEGATIVE")
  elif (b % 2 == 0) and (b < 0):
    print("EVEN NEGATIVE")
  
  elif (b == 0):
    print("NULL")
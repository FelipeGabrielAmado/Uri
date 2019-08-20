fim = int(0)

while (fim!=1):
  p = input().split()
  x, y = p
  x = float(x)
  y = float(y)
  if x == 0:
      fim = 1
  if y == 0:
      fim = 1
  if x > 0:
      if y > 0:
          print('primeiro')
      if y < 0:
          print('quarto')
  if x < 0:
      if y > 0:
          print('segundo')
      if y < 0:
          print('terceiro')
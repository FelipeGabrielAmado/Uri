A = int(input())
for x in range(1, A+1):
  a,b,c = map(float, input().split())
  a = a * 0.2
  b = b * 0.3
  c = c * 0.5
  media = float(a+b+c)
  print("%0.1f" %media)
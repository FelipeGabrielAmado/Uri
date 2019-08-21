total = float(0)
for x in range (int(input())):
  n1, n2 = list(map(int,input().split()))
  if(n1 == 1001):
    total+= 1.50 * n2
  if(n1 == 1002):
    total+= 2.50 * n2
  if(n1 == 1003):
    total+= 3.50 * n2
  if(n1 == 1004):
    total+= 4.50 * n2
  if(n1 == 1005):
    total+= 5.50 * n2

print('%0.2f'%total)
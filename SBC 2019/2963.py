    v = []
for x in range(int(input())):
  n = int(input())
  v.append(n)

for y in range(len(v)):
  if(v[0] < v[y]):
    flag = True
    break
  else:
    flag = False

if(flag == True):
  print('N')
else:
  print('S')
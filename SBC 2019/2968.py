A = list(map(int,input().split()))
x, y = A
z = x*y
aux = int()
v = []

for x in range(1, 10):
  aux = round(((z*x)/10)+0.49)
  v.append(aux)

print(*v)
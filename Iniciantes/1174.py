vet = []
pos = []
for x in range (100):
  n = float(input())
  vet.append(n)
  pos.append(x)

for y in range (100):
  if ( vet[y] <=10):
    print('A[{}] = {}'.format(pos[y],vet[y]))
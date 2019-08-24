vetor = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
  y = int(input())
  if(y > 0):
    vetor[x] = y
  else:
    vetor[x] = 1

for z in range(10):
  print("X[{}] = {}".format(z, vetor[z]))
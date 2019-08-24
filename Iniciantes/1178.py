A = float(input())
V = []
for x in range(0,100):
  V.append(A)
  print('N[{}] = {:0.4f}'.format(x, A))
  A -= A/2
anao = 0
elfo = 0
humano = 0
mago = 0
hobbit = 0

for x in range(int(input())):
  A = list(input().split())
  a, b = A
  if (b == 'A'):
    anao+= 1
  elif (b == 'E'):
    elfo += 1
  elif (b == 'H'):
    humano += 1
  elif(b == 'M'):
    mago += 1
  elif(b == 'X'):
    hobbit += 1

print('{} Hobbit(s)'.format(hobbit))
print('{} Humano(s)'.format(humano))
print('{} Elfo(s)'.format(elfo))
print('{} Anao(s)'.format(anao))
print('{} Mago(s)'.format(mago))
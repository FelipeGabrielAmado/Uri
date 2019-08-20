i,f=map(int, input().split())
if (i > f):
  i = 24 - i
  h = i + f
  print("O JOGO DUROU %d HORA(S)" %h)

elif (i < f):
  h = f - i
  print("O JOGO DUROU %d HORA(S)" %h)

elif (i == f):
  h = 24
  print("O JOGO DUROU %d HORA(S)" %h)
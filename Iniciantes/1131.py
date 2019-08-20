op = int(1)
inter = int(0)
gremio = int(0)
empate = int(0)
grenais = int(0)

while (op != 2):
  i,g=map(int, input().split())
  
  if(i>g):
    inter += 1
  elif(g>i):
    gremio += 1
  else:
    empate += 1
  
  print("Novo grenal (1-sim 2-nao)")
  op = int(input())
  grenais += 1

print("%d grenais" %grenais)
print("Inter:%d" %inter)
print("Gremio:%d" %gremio)
print("Empates:%d"%empate)

if(inter>gremio):
  print("Inter venceu mais")
elif(gremio>inter):
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")
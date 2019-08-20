contador = int(0)
positivo = int(0)
media = float(0)

while (contador < 6):
  A = float(input())
  if A >= 0:
    positivo = positivo + 1
    media = media + A
  contador += 1

media = media / positivo

print("%d valores positivos"%positivo)
print("%0.1f" %media)
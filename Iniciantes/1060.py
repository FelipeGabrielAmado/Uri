contador = 0
positivo = int(0)

while (contador < 6):
    A = float(input())
    contador += 1
    if (A > 0):
      positivo += 1


print("%d valores positivos"%positivo)
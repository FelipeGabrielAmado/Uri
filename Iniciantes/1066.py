par = int(0)
impar = int(0)
positivo = int(0)
negativo = int(0)

for x in range(1, 6):
  A = int(input())
  if (A % 2 == 0):
    par += 1
  if (A % 2 == 1):
    impar += 1
  if (A > 0):
    positivo+= 1
  if (A < 0):
    negativo += 1

print("%s valor(es) par(es)"%par)
print("%s valor(es) impar(es)"%impar)
print("%s valor(es) positivo(s)"%positivo)
print("%s valor(es) negativo(s)"%negativo)
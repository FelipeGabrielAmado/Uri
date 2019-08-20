op = int(input())
alcool = int(0)
gasolina = int(0)
diesel = int(0)

while op != 4:
  op = int(input())
  if (op == 1):
    alcool += 1 
  elif (op == 2):
    gasolina += 1
  elif (op == 3):
    diesel += 1

print("MUITO OBRIGADO")
print("Alcool: %s" %alcool)
print("Gasolina: %s" %gasolina)
print("Diesel: %s" %diesel)
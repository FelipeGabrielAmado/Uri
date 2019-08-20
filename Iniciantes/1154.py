op = int(0)
total = float(0)
cont = int(-1)

while (op >= 0):
 total += op
 op = int(input())
 cont+=1

resultado = float(total/cont)
print("%0.2f"%resultado)
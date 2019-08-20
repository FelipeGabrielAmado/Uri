import math
P1 = input().split(" ")
P2 = input().split(" ")

x1, y1 = P1
x2, y2 = P2

distancia = math.sqrt(((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2))

print("%0.4f"%distancia)
valor = int(input())
val = valor

cem = int(valor/100)
valor = valor % 100

cinquenta = int(valor/50)
valor = valor % 50

vinte = int(valor/20)
valor = valor % 20

dez = int(valor/10)
valor = valor % 10

cinco = int(valor/5)
valor = valor % 5

dois = int(valor/2)
valor = valor % 2

um = int(valor/1)
valor = valor % 1

print(val)
print("%d nota(s) de R$ 100,00"%cem)
print("%d nota(s) de R$ 50,00"%cinquenta)
print("%d nota(s) de R$ 20,00"%vinte)
print("%d nota(s) de R$ 10,00"%dez)
print("%d nota(s) de R$ 5,00"%cinco)
print("%d nota(s) de R$ 2,00"%dois)
print("%d nota(s) de R$ 1,00"%um)
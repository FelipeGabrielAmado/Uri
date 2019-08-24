x1, x2, x3, x4, x5, x6, x7, x8, x9 = list(map(int,input().split()))
renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

soma = x1 +x2 + x3 + x4 + x5 +x6 +x7 +x8+ x9

while(soma>=10):
  soma-=9

print(renas[soma-1])
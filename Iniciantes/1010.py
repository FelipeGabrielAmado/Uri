A = input().split(" ")
B = input().split(" ")

code1, qt1, vlr1 = A
code2, qt2, vlr2 = B

total = (int(qt1) * float(vlr1))+ (int(qt2)* float(vlr2))

print("VALOR A PAGAR: R$ %0.2f" %total)
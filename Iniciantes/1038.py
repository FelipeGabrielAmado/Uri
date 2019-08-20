op,qt = map(int, input().split())


if op == 1:
  valor = 4.00 * qt
  print("Total: R$ %0.2f" %valor)
elif op == 2:
  valor = 4.50 * qt
  print("Total: R$ %0.2f" %valor)
elif op == 3:
  valor = 5.00 * qt
  print("Total: R$ %0.2f" %valor)
elif op == 4:
  valor = 2.00 * qt
  print("Total: R$ %0.2f" %valor)
elif op == 5:
  valor = 1.50 * qt
  print("Total: R$ %0.2f" %valor)

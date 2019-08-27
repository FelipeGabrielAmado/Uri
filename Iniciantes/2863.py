aux = float(99999999)
while True:
  try:
    for x in range(int(input())):
      A = float(input())
      if(A < aux):
        aux = A
    print("{:.2f}".format(aux))
    aux = float(99999999)

  except EOFError:
    break
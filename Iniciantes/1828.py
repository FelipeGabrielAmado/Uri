for x in range (int(input())):
  A = input().split(" ")
  a, b = A
  if(a == "tesoura" and b == "papel"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "papel" and b == "tesoura"):
    print("Caso #{}: Raj trapaceou!".format(x+1))
  
  elif(a == "papel" and b == "pedra"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "pedra" and b == "papel"):
    print("Caso #{}: Raj trapaceou!".format(x+1))
  
  elif(a == "pedra" and b == "lagarto"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "lagarto" and b == "pedra"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "lagarto" and b == "Spock"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "Spock" and b == "lagarto"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "Spock" and b == "tesoura"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "tesoura" and b == "Spock"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "tesoura" and b == "lagarto"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "lagarto" and b == "tesoura"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "lagarto" and b == "papel"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "papel" and b == "lagarto"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "papel" and b == "Spock"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "Spock" and b == "papel"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "Spock" and b == "pedra"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "pedra" and b == "Spock"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif(a == "pedra" and b == "tesoura"):
    print("Caso #{}: Bazinga!".format(x+1))
  elif(a == "tesoura" and b == "pedra"):
    print("Caso #{}: Raj trapaceou!".format(x+1))

  elif (a == b):
    print("Caso #{}: De novo!".format(x+1))
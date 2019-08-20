salarioi = float(input())
if(salarioi <= 400):
  aumento = salarioi * 0.15
  novosalario = salarioi + aumento
  print("Novo salario: %0.2f" %novosalario)
  print("Reajuste ganho: %0.2f" %aumento)
  print("Em percentual: 15 %")

elif(salarioi > 400 and salarioi <= 800):
  aumento = salarioi * 0.12
  novosalario = salarioi + aumento
  print("Novo salario: %0.2f" %novosalario)
  print("Reajuste ganho: %0.2f" %aumento)
  print("Em percentual: 12 %")

elif(salarioi > 800 and salarioi <= 1200):
  aumento = salarioi * 0.10
  novosalario = salarioi + aumento
  print("Novo salario: %0.2f" %novosalario)
  print("Reajuste ganho: %0.2f" %aumento)
  print("Em percentual: 10 %")

elif(salarioi > 1200 and salarioi <= 2000):
  aumento = salarioi * 0.07
  novosalario = salarioi + aumento
  print("Novo salario: %0.2f" %novosalario)
  print("Reajuste ganho: %0.2f" %aumento)
  print("Em percentual: 7 %")

elif(salarioi > 2000):
  aumento = salarioi * 0.04
  novosalario = salarioi + aumento
  print("Novo salario: %0.2f" %novosalario)
  print("Reajuste ganho: %0.2f" %aumento)
  print("Em percentual: 4 %")
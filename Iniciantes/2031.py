x = int(input())
while x != 0:
  a = input()
  b = input()

  if (a == 'ataque' and b == 'pedra'):
    print('Jogador 1 venceu')
  
  elif (a == 'ataque' and b == 'papel'):
    print('Jogador 1 venceu')
  
  elif (a == 'ataque' and b == 'ataque'):
    print('Aniquilacao mutua')

  elif (a == 'pedra' and b == 'ataque'):
    print('Jogador 2 venceu')
  
  elif (a == 'pedra' and b == 'papel'):
    print('Jogador 1 venceu')

  elif (a == 'pedra' and b == 'pedra'):
    print('Sem ganhador')

  elif (a == 'papel' and b == 'ataque'):
    print('Jogador 2 venceu')

  elif(a == 'papel' and b == 'pedra'):
    print('Jogador 2 venceu')

  elif(a == 'papel' and b == 'papel'):
    print('Ambos venceram')
  x-=1
while True:
  try:
    for x in range(int(input())):
      A = input()
      if(A == '.'):
        print('a')
      elif(A == '..'):
        print('b')
      elif(A == '...'):
        print('c')
      elif(A == '. .'):
        print('d')
      elif(A == '.. ..'):
        print('e')
      elif(A == '... ...'):
        print('f')
      elif(A == '. . .'):
        print('g')
      elif(A == '.. .. ..'):
        print('h')
      elif(A == '... ... ...'):
        print('i')
      elif(A == '. . . .'):
        print('j')
      elif(A == '.. .. .. ..'):
        print('k')
      elif(A == '... ... ... ...'):
        print('l')
      elif(A == '. . . . .'):
        print('m')
      elif(A == '.. .. .. .. ..'):
        print('n')
      elif(A == '... ... ... ... ...'):
        print('o')
      elif(A == '. . . . . .'):
        print('p')
      elif(A == '.. .. .. .. .. ..'):
        print('q')
      elif(A == '... ... ... ... ... ...'):
        print('r')
      elif(A == '. . . . . . .'):
        print('s')
      elif(A == '.. .. .. .. .. .. ..'):
        print('t')
      elif(A == '... ... ... ... ... ... ...'):
        print('u')
      elif(A == '. . . . . . . .'):
        print('v')
      elif(A == '.. .. .. .. .. .. .. ..'):
        print('w')
      elif(A == '... ... ... ... ... ... ... ...'):
        print('x')
      elif(A == '. . . . . . . . .'):
        print('y')
      elif(A == '.. .. .. .. .. .. .. .. ..'):
        print('z')
  except EOFError:
    break
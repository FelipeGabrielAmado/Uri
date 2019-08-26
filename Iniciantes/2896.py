for x in range (int(input())):
  a, b = list(map(int,input().split()))
  ganho = a / b
  sobra = a % b
  print(int(ganho+sobra))
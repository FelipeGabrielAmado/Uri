A = int(input())
for x in range(1, A+1):
  a,b = map(int, input().split())
  if (b == 0):
    print("divisao impossivel")
  else:
    media = a/b
    print(media)
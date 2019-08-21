x = int(input())
A,B,C,D,E = map(int, input().strip().split())
contador = int(0)
if(x == A):
  contador+=1
if(x == B):
  contador+=1
if(x == C):
  contador+=1
if(x == D):
  contador+=1
if(x == E):
  contador+=1

print(contador)
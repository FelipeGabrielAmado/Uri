A = list(map(int,input().split()))
x, y, z = A
aux = x / (y+z)
print('{:0.2f}'.format(aux))
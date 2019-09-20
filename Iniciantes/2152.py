for x in range(int(input())):
    A = list(map(int,input().split()))
    a, b, c = A
    if(c == 0):
        print('{:02d}:{:02d} - A porta fechou!'.format(a,b))
    elif(c == 1):
        print('{:02d}:{:02d} - A porta abriu!'.format(a,b))
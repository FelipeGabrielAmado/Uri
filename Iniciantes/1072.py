A = int(input())
inside = int(0)
outside = int(0)

for x in range(1, A+1):
   x1 = int(input())
   if x1 >= 10 and x1 <=20:
     inside+= 1 
   else:
     outside+= 1

print("%d in" %inside)
print("%d out" %outside)
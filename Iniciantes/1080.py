A = int(0)
pos = int(0)
val = int(0)

for x in range(1, 101):
  A = int(input())
  if (A > val):
    val = A
    pos = x

print(val)
print(pos)
import math

n = int(input())
a = 0
for i in range(1, n+1):
    a += int(math.sqrt(i))
print(a)
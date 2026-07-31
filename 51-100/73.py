import math

n = int(input()) 
s = 0

for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        s += 2
        if i * i == n:
            s -= 1
print(s)
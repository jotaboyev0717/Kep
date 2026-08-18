import math

n = int(input())
count = 0

x = 1
while x * x <= n:
    y_max = math.isqrt(n - x * x)
    count += y_max
    x += 1

print(count)
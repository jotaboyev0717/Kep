import math

n = int(input())

for num in range(2, n + 1):
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')

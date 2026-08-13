n = int(input())
p = int(input())

s = 1
for i in range(1, n + 1):
    s *= i

print(s % p)
n = int(input())

sieve = [True] * (n + 1)

for i in range(2, n + 1):
    if sieve[i]:
        for j in range(i * i, n + 1, i):
            sieve[j] = False

print(*[i for i in range(2, n + 1) if sieve[i]])
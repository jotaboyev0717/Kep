n = int(input())
p = int(input())

s = 1
if n > p:
    print(0)
else:
    for i in range(1, n + 1):
        s = (s * i) % p
    print(s)
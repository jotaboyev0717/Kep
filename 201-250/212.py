n = int(input())
s = 0
m = 5
while n > m:
    s += n // m
    m *= 5

print(s)
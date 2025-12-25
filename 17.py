result = []
for i in range(1000, 10000):
    a = str(i)
    s = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
    if s % 2 == 0:
        result.append(a)
print(' '.join(result))
n = int(input())
count = 0
for i in range(1, n + 1):
    if i * i > n:
        break
    for y in range(1, n + 1):
        if i ** 2 + y ** 2 <= n:
            count += 1
        else:
            break
print(count)


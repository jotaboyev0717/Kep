n = int(input())
for i in range(1, n+1):
    if n % (2 * i + 1) == 0:
        print('Yes')
        break
else:
    print('No')

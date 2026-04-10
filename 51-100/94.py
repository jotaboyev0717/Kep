for i in range(100, 1000):
    a = str(i)
    sum1 = int(a[0]) * int(a[1]) * int(a[2])
    if sum1 == 0:
        continue
    elif i % sum1 == 0:
        print(i)
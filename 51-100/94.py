for i in range(100, 1000):
    a = str(i)
    product = int(a[0]) * int(a[1]) * int(a[2])
    total = int(a[0]) + int(a[1]) + int(a[2])
    if product % total == 0:
        print(i)
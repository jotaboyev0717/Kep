for i in range(1000, 10000):
    a  = int(str(i)[::-1])
    if i == a * 4:
        print(a)
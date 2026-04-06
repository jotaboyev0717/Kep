for i in range(100, 1000):
    i = str(i)
    if (int(i[0]) * int(i[1]) * int(i[2])) % (int(i[0]) + int(i[1]) + int(i[2])) == 0:
        print(i)
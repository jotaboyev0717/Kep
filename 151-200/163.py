n = input()
b = int(input())
len_n = len(n)
if len_n < 2:
    if int(n) == b:
        print('B')
    else:
        print('N')
else:
    s = 0
    m = 1
    for i in range(len_n):
        s += int(n[i])
        m *= int(n[i])

    if s == b and m == b:
        print('B')
    elif m == b:
        print('P')
    elif s == b:
        print('S')
    else:
        print('N')








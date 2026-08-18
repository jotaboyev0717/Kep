a = int(input())
s = 0
for _ in range(a):
    b = int(input())
    if b <= 35000:
        s += b * 0.8
    elif b <= 350000:
        s += b * 0.88
    else:
        s += b * 0.93
print(round(s, 1))
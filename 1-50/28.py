a = int(input())
for i in range(a):
    s = input()
    if len(s)>10:
        print(s[0]+s[-1])
    else:
        print(s)
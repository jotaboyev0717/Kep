b = input()
s = 0
for i in b:
    if 'a' <= i.lower() <= 'z':
        s += 1
print(s)
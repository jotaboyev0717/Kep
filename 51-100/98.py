a = input()
b = input()
s = 0
for i in a:
    if i in b:
        s += 1
if len(a) == len(b) == s:
    print(True)
else:
    print(False)

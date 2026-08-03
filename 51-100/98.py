a = list(input())
b = list(input())
s = 0
for i in a:
    if i in b:
        b.remove(i)
        s += 1
if len(a) == s:
    print(True)
else:
    print(False)

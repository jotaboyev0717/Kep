a = input()
b = input()
found = False
for i in range(len(a)):
    if a[i] in b:
        found = True
        break
print(found)
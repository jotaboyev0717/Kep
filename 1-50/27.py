a = input()
if a.isupper():
    print(True)
elif a[0].islower() and a[1:].isupper():
    print(True)
else:
    print(False)
a = input()

try:
    int(a)
    print('Yes')
except ValueError:
    print('No')
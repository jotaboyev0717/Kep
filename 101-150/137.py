a = input()
b = input()

try:
    c = int(a)
    d = int(b)
    if d == 0:
        print('inf')
    else:
        print(c // d)
except ValueError:
    print("Wrong Format")
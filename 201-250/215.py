import math
arr = list(map(int, input().split()))
result = math.gcd(arr[0], arr[1])
if arr[2] % result == 0:
    print('Yes')
else:
    print('No')
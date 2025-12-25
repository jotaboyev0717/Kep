# import math

# n = int(input())
# a = []
# if n <= 1:
#     print("No")
# else:
#     for i in range(2, math.isqrt(n) + 1):
#         if n % i == 0:
#             print("No")
#             break
#     else:
#         print(i)

import math

n = int(input())

for num in range(2, n + 1):
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        print(num)

import math
n = int(input())
m = math.isqrt(n)

total_sum = 0

for k in range(1, m):
   count = 2 * k + 1
   total_sum += k * count

remaining_numbers = n - (m * m) + 1
total_sum += remaining_numbers * m

print(total_sum)

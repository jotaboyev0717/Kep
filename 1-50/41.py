from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

count = Counter(nums)
max_freq = max(count.values())

modes = [k for k, v in count.items if v == max_freq]
print(min(modes))


n = int(input())
nums = list(map(int, input().split()))
found = False
for i, num in enumerate(nums):
    if num == 1:
        print(i)
        found = True
        break

if not found:
    print(-1)
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
result = -1
for i, num in enumerate(numbers):
    if num == 1:
        count += 1
        if count == k:
            result = i
            break
print(result)
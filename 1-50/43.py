n = int(input())
numbers = list(map(int, input().split()))

count = 0
result = -1

for i, number in enumerate(numbers):
    if number == 1:
        count += 1
        if count == 2:
            result = i
            break
        
print(result)
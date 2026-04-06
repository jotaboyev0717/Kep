n = int(input())
arr = list(map(int, input().split()))
c1 = 0
c2 = 0
c3 = 0

result1 = -1
result2 = -1
result3 = -1

for i in range(len(arr)):
    if arr[i] == 1:
        c1 += 1
        if c1 == 1:
            result1 = i + 1
    elif arr[i] == 2:
        c2 += 1
        if c2 == 2:
            result2 = i + 1
    elif arr[i] == 3:
        c3 += 1
        if c3 == 3:
            result3 = i + 1
            
print(result1, result2, result3)
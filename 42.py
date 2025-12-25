n = int(input())
numbers = list(map(int, input().split()))
index_n = -1
for i in range(n):
    if numbers[i] == 1:
        index_n = i+1
        break
print(index_n)


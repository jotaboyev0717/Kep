n = int(input())
arr_1 = list(map(int, input().split()))
counts = {}
for num in arr_1:
    counts[num] = counts.get(num, 0) + 1


m = int(input())
for _ in range(m):
    x = int(input())
    print(counts.get(x, 0))
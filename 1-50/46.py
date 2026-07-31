n = int(input())
arr = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    x = int(input())
    print(x in arr)
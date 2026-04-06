n = int(input())
numbers = list(map(int, input().split()))

if 1 in numbers:
    print(numbers.index(1))
else:
    print(-1)
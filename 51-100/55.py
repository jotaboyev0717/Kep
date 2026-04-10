n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    return sum(int(d) for d in str(x))

def first_digit(x):
    return int(str(x)[0])

arr.sort(key=lambda x: (digit_sum(x), first_digit(x), x))

print(*arr)
n = int(input())
x = [int(input()) for _ in range(n)]
arith = sum(x) / len(x)
print(*sorted(i for i in x if i > arith))
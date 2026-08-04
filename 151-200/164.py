n = int(input())

s = 0
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    s += matrix[i][i]

print(s)
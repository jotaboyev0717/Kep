n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

row_1 = sum(matrix[0])
row_last = sum(matrix[-1])
column_1 = sum([i[0] for i in matrix]) - matrix[0][0] - matrix[0][-1]
column_last = sum([i[-1] for i in matrix]) - matrix[-1][0] - matrix[-1][-1]
print(row_1 + row_last + column_1 + column_last)
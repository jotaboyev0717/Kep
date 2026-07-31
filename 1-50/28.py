n = int(input())
empty = []
for _ in range(n):
    empty.append(input())

for i in empty:
    if len(i) > 10:
        print(i[0] + i[-1])
    else:
        print(i)


n = int(input())
list_1 = list(map(int, input().split()))
a = []
for i in list_1:
    if list_1.count(i) == 3:
        a.append(i)

print(a)
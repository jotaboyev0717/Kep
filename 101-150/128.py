from collections import Counter
n = int(input())
arr = list(map(int, input().split()))

total_count = Counter(arr)

dic = {}
fin = []
for num in arr:
    dic[num] = dic.get(num, 0) + 1
    if dic[num] == 3 and total_count[num] == 3:
        fin.append(num)
print(*fin)

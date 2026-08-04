a = input()

for i in range(1, len(a)):
    part_1 = a[:i]
    part_2 = a[i:]
    if part_1 == part_1[::-1] and part_2 == part_2[::-1]:
        print('Yes')
        break
else:
    print('No')

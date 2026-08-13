# n = int(input())
# arr = list(map(int, input().split()))
# c1 = 0
# c2 = 0
# c3 = 0
#
# result1 = -1
# result2 = -1
# result3 = -1
#
# for i in range(len(arr)):
#     if arr[i] == 1:
#         c1 += 1
#         if c1 == 1:
#             result1 = i + 1
#     elif arr[i] == 2:
#         c2 += 1
#         if c2 == 2:
#             result2 = i + 1
#     elif arr[i] == 3:
#         c3 += 1
#         if c3 == 3:
#             result3 = i + 1
#
# print(result1, result2, result3)

# n = int(input())
# arr = list(map(int, input().split()))
# count1 = 0
# count2 = 0
# count3 = 0
# for i, sel in enumerate(range(n)):
#     if sel == 1:
#         count1 += 1
#         if count1 == 1:
#             a = i
#     elif sel == 2:
#         if count2 == 2:
#             b = i
#         count2 += 1
#
#     elif sel == 3:
#         if count3 == 3:
#             c = i
#         count3 += 1
# print(a, b, c)

n = int(input())
arr = list(map(int, input().split()))
c1 = 0
c2 = 0
c3 = 0

r1 = -1
r2 = -1
r3 = -1

for i in range(len(arr)):
    if arr[i] == 1:
        c1 += 1
        if c1 == 1:
            r1 = i + 1
    elif arr[i] == 2:
        c2 += 1
        if c2 == 2:
            r2 = i + 1
    elif arr[i] == 3:
        c3 += 1
        if c3 == 3:
            r3 = i + 1

print(r1, r2, r3)


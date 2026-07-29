# n = int(input())
# for i in range(2, n):
#     for a in range(2, i):
#         if i % a == 0:
#             break
#     else:
#         print(i)

print(*[i for i in range(2, int(input())) if all(i % a == 0 for a in range(2, i))])
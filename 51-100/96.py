n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()
if len(s) % 2 != 0:
    print(s[len(s) // 2])
else:
    print(s[len(s) // 2 - 1])
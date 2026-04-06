n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])
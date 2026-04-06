a = int(input())
s = []
t = 0
for i in range(a):
    s.append(int(input()))
for i in s:
    if i % 2:
        t += i
        
print(t)
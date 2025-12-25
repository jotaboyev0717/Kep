a = int(input())
b = int(input())
count = 0
start = min(a,b)
end = max(a, b)
for i in range(start, end+1):
    if i % 4 == 0:
        count+=1
print(count)
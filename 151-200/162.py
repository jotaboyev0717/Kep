n = input()

s = 0
for i in n:
    try:
        int(i)
        s+=1
    except:
        continue
print(s)

a = input()
s = 0
for i in a:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z' :
        s+=1
print(s)
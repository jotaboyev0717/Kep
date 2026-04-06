son = input()
count = 0
for c in reversed(son):
    if c == '0':
        count += 1
    else:
        break
    
print(count)
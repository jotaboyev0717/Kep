n = int(input())
for k in range(1, n + 1):
    if k % 3 == 1:
        repeat = 1
    elif k % 3 == 2:
        repeat = 2
    else:
        repeat = 3
        
    for _ in range(repeat):
        print(k, end=' ')
    

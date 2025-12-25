n = int(input())

if n <= 9:
    print(n)
else:
    count_nines = n // 9
    remainder = n % 9
    
    if remainder == 0:
        print('9' * count_nines)
    else:
        print(str(remainder) + '9' * count_nines)
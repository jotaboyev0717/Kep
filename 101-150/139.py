n = int(input())
try:
    if n < 1:
        raise ValueError

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if n < 2:
        is_prime = False
    print('Prime' if is_prime else 'Not Prime')
except ValueError:
    print("Wrong Format")
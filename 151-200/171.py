def last_primes(n):
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, num ** 0.5 + 1):
            if num % i:
                is_prime = False
                break

        if is_prime:
            count += 1
            yield num
        num += 1


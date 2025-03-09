primes = []

for n in range(2, 100):
    is_prime = True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(n)

print("Liczby pierwsze mniejsze niż 100:", primes)

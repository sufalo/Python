def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    fac = 1
    for i in range(2, n + 1):
        fac *= i

    return fac

print(factorial(5))
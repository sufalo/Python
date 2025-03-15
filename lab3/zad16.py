def fibonacci(n):
    if n < 0:
        raise ValueError("Indeks nie może być ujemny")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

print(fibonacci(13))
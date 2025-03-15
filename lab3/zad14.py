def czy_liczba_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

print(czy_liczba_pierwsza(2))
print(czy_liczba_pierwsza(17))
print(czy_liczba_pierwsza(18))
print(czy_liczba_pierwsza(1))
print(czy_liczba_pierwsza(29))

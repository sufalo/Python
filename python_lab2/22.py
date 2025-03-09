n = int(input("Podaj liczbę (od 1 do 26) dla wielkości słownika: "))

if 1 <= n <= 26:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dictionary = {alphabet[i]: (i + 1) ** 2 for i in range(n)}
    
    print("Stworzony słownik:", dictionary)
else:
    print("Proszę podać liczbę w zakresie od 1 do 26.")

liczba = int(input("Podaj liczbę: "))

i = 0
jest_kwadratem = False

while i * i <= liczba:
    if i * i == liczba:
        jest_kwadratem = True
        break
    i += 1

if jest_kwadratem:
    print(f"Liczba {liczba} jest kwadratem liczby naturalnej.")
else:
    print(f"Liczba {liczba} nie jest kwadratem liczby naturalnej.")

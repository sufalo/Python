
import math

def mediana(lista):
    lista_sort = sorted(lista)
    n = len(lista)
    srodek = n // 2

    if(n%2 == 0):
        return lista_sort[srodek - 1] + lista_sort[srodek + 1] / 2
    else:
        return lista_sort[srodek]

def srednia(lista):
    return sum(lista)/ len(lista)

def min(lista):
    min = lista[0]
    for liczba in lista:
        if liczba < min:
            min = liczba

    return min

def max(lista):
    max = lista[0]
    for liczba in lista:
        if liczba > max:
            max = liczba

    return max

def std_var(lista):
    if len(lista) < 2:
        return 0

    avg = srednia(lista)
    suma_kwadratow = sum((x - avg) ** 2 for x in lista)
    return math.sqrt(suma_kwadratow / (len(lista) - 1))

def statystyki_listy(lista):
    if not lista:
        raise ValueError("Lista nie może być pusta!")

    return {
        "Średnia": srednia(lista),
        "Mediana": mediana(lista),
        "Minimum": min(lista),
        "Maksimum": max(lista),
        "Odchylenie standardowe": std_var(lista)
    }

liczby = [10, 20, 30, 40, 50]
wynik = statystyki_listy(liczby)

for klucz, wartosc in wynik.items():
    print(f"{klucz}: {wartosc}")
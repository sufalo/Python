def sortuj(kierunek, lista):
    n = len(lista)

    if kierunek == "desc":
        for i in range(n):
            for j in range(n - 1 - i):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    else:
        for i in range(n):
            for j in range(n - 1 - i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

liczby = [5, 3, 8, 1, 2, 7]

print("Sortowanie rosnące:", sortuj("desc", liczby[:]))
print("Sortowanie malejące:", sortuj("asc", liczby[:]))
def szukajWLiscie(lista, a):
    cnt = 0
    for liczba in lista:
        if(liczba == a):
            cnt+=1

    return cnt

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2]

print(szukajWLiscie(lista, 2))
D = {"a": 1, "b": 2, "abc": 32, "fatal": 66, "xyz": "ijk"}

klucz = input("Podaj klucz: ")

if klucz in D:
    print(f"Wartość dla klucza '{klucz}' to: {D[klucz]}")
else:
    nowa_wartosc = input(f"Klucz '{klucz}' nie istnieje. Podaj wartość dla tego klucza: ")
    D[klucz] = nowa_wartosc
    print(f"Nowy element został dodany: {klucz}: {nowa_wartosc}")

print("Zaktualizowany słownik:", D)

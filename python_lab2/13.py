tekst = input("Podaj ciąg znaków: ")

if len(tekst) >= 4:
    wynik = tekst[:2] + tekst[-2:]
    print("Wynik:", wynik)
else:
    print("Ciąg znaków jest za krótki, aby wyciągnąć dwie pierwsze i dwie ostatnie litery.")

try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    suma = a + b
    print("Suma liczb:", suma)
    
except ValueError:
    print("Błąd: Wprowadź poprawne liczby całkowite!")

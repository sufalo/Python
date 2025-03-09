a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b**2 - 4*a*c

if delta > 0:
    print("Funkcja ma dwa różne miejsca zerowe.")
elif delta == 0:
    print("Funkcja ma jedno miejsce zerowe (podwójne).")
else:
    print("Funkcja nie ma miejsc zerowych.")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Trojkat istnieje")
else:
    print("Trojkat nie istnieje")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

if a > b and a > c:
    print(a)
elif b > c and b > c:
    print(b)
else:
    print(c)
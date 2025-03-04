a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)

#

numbers = []

for i in range(3):
    num = int(input(f"Podaj liczbę {i+1}: "))
    numbers.append(num)

numbers.sort()

print(*numbers)

import math

def rysuj_kolo(promien):
    for i in range(-promien, promien + 1):
        for j in range(-promien, promien + 1):
            if i ** 2 + j ** 2 <= promien ** 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    pole = math.pi * promien ** 2
    print(f'Pole koła: {pole:.2f}')

def rysuj_kwadrat(bok):
    for i in range(bok):
        for j in range(bok):
            print('*', end='')
        print()
    pole = bok ** 2
    print(f'Pole kwadratu: {pole}')

print("Koło:")
rysuj_kolo(5)

print("\nKwadrat:")
rysuj_kwadrat(4)

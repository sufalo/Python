import math

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

def czy_wspolliniowe(P1, P2, P3):
    return (P2[0] - P1[0]) * (P3[1] - P1[1]) == (P3[0] - P1[0]) * (P2[1] - P1[1])

def obwod_trojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Ostrzeżenie: Punkty są współliniowe i nie tworzą trójkąta.")
        return 0
    
    a = odleglosc(P1, P2)
    b = odleglosc(P2, P3)
    c = odleglosc(P3, P1)
    
    return a + b + c

P1 = (0, 0)
P2 = (3, 0)
P3 = (0, 4)
print("Obwód trójkąta:", obwod_trojkata(P1, P2, P3))

P1 = (0, 0)
P2 = (1, 1)
P3 = (2, 2)
print("Obwód trójkąta:", obwod_trojkata(P1, P2, P3))

import math

def odleglosc(P1, P2):
    return(math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2))

def obwodTrojkata(P1, P2, P3):
    a = odleglosc(P1, P2)
    b = odleglosc(P2, P3)
    c = odleglosc(P3, P1)

    return(a + b + c)

P1 = (0, 0)
P2 = (3, 0)
P3 = (0, 4)

print(obwodTrojkata(P1, P2, P3))
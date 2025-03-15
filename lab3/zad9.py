def czyWspolliniowe(P1, P2, P3):
    if(P2[0] - P1[0]) * (P3[1] - P1[1]) == (P3[0] - P1[0]) * (P2[1] - P1[1]):
        print("Punkty są współliniowe i nie tworzą trójkąta.")
        return False
    else:
        return True

P1 = (0, 0)
P2 = (1, 1)
P3 = (2, 2)
print(czyWspolliniowe(P1, P2, P3))

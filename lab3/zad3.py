def dach(znak):
    print(f"  {znak*8}")
    print(f" {znak*10}")
    print(f"{znak*12}")

def pietro(znak):
    print(f"|{znak*10}|")
    print(f"|  []  []  |")
    print(f"|{znak*10}|")

dach("*")
pietro("#")
pietro("=")

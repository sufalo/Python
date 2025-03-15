def dach(znak):
    print(f"  {znak*10}")
    print(f" {znak*12}")
    print(f"{znak*14}")

def pietro(pietra, znak):
    for _ in range(pietra):
        print(f"|{znak*3}[]{znak*2}[]{znak*3}|")

def rysuj_dom(pietra, znak1, znak2):
    dach(znak2)
    pietro(pietra, znak1)

rysuj_dom(12, "*", "#")
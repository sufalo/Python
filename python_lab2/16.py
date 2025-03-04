l = ['a']

while True:
    znak = input("Podaj znak (wpisz 'stop', aby zakończyć): ")
    
    if znak == 'stop':
        break
    
    l.append(znak)

print(l)
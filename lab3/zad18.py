def konwertuj_temperature(temp, skala_wej, skala_wyj):
    if skala_wej == 'C':
        celsius = temp
    elif skala_wej == 'F':
        celsius = (temp - 32) * 5 / 9
    elif skala_wej == 'K':
        celsius = temp - 273.15
    else:
        raise ValueError("Nieznana skala wejściowa.")
    
    if skala_wyj == 'C':
        return celsius
    elif skala_wyj == 'F':
        return celsius * 9 / 5 + 32
    elif skala_wyj == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Nieznana skala wyjściowa.")

print(konwertuj_temperature(100, 'C', 'F'))
print(konwertuj_temperature(32, 'F', 'C')) 
print(konwertuj_temperature(0, 'C', 'K'))  
print(konwertuj_temperature(300, 'K', 'C'))

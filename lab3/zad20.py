def szyfruj_tekst(tekst, klucz):
    zaszyfrowany_tekst = ""
    
    for znak in tekst:
        if 'a' <= znak <= 'z':
            zaszyfrowany_tekst += chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
        elif 'A' <= znak <= 'Z':
            zaszyfrowany_tekst += chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
        else:
            zaszyfrowany_tekst += znak
    
    return zaszyfrowany_tekst

tekst = "Witaj, świecie!"
klucz = 3
print(f"Zaszyfrowany tekst: {szyfruj_tekst(tekst, klucz)}")

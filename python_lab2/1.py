D = {"imię": "Jan", "nazwisko": "Nowak", "wiek": 20, "wzrost": 185}
print(D.keys())
print(D.items())
print(len(D))

D["waga"] = 75

print(f"{D['imię']}-{D['wiek']}!!!")

D["wzrost"] = 178

print(D)
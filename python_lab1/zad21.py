liczba = int(input("Podaj liczbę: "))

cyfra_jednosci = liczba % 10
cyfra_dziesiatek = (liczba // 10) % 10
cyfra_setek = (liczba // 100) % 10

print(f"Cyfra jedności: {cyfra_jednosci}")
print(f"Cyfra dziesiątek: {cyfra_dziesiatek}")
print(f"Cyfra setek: {cyfra_setek}")

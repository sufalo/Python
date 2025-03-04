import random

target_number = random.randint(13, 99)

attempts = 0

print("Zgadnij liczbę od 13 do 99. Jeśli chcesz zakończyć, wpisz 'q'.")

while True:
    user_input = input("Podaj swoją liczbę: ")

    if user_input.lower() == 'q':
        print(f"Program zakończony. Szukana liczba to {target_number}. Liczba prób: {attempts}.")
        break

    try:
        user_number = int(user_input)
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")
        continue

    attempts += 1

    if user_number == target_number:
        print(f"Gratulacje! Odgadłeś liczbę {target_number} w {attempts} próbach.")
        break
    elif user_number < target_number:
        print("Twoja liczba jest za mała. Spróbuj ponownie.")
    else:
        print("Twoja liczba jest za duża. Spróbuj ponownie.")

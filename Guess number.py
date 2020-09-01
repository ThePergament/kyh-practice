import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1-100, gissa vilket?")

while True:
    text = input("Din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Rätt!")
        break

    if as_number < n:
        print("Fel! Mitt  nummer är högre...försök igen!")

    if as_number > n:
        print("Fel! Mitt nummer är lägre...Försök igen!")
import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1-100, gissa vilket?")
guesses =1


def mainloop(guesses):
    n = random.randint(1, 100)
    while True:
        text = input("Din gissning: ")
        as_number = int(text)

        if as_number == n:
            print("Bra jobbat! Det tog" +str (guesses)+"gissningar!")

            break


        if as_number < n:
            print("Fel! Mitt  nummer är högre...försök igen!")
            guesses = guesses + 1

        if as_number > n:
            print("Fel! Mitt nummer är lägre...Försök igen!")
            guesses = guesses + 1

mainloop(guesses)
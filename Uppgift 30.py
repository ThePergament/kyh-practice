#Träna slicing av strängar och listor!
#Reg.nr på bilar i Sverge skrivs traditionellt* med tre bokstäver och tre siffror.
#1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
#var för sig; använd slicing-syntax för att dela upp inputsträngen.
#Ex.
#Ange regnr: ABC663
#Bokstävsgrupp: ABC
#Siffergrupp: 663
#2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
    #Ange tal med komma emellan: 1,2,3,5,100
    #Första talet: 1
    #Sista talet: 100
    #Summan av talen: 111
    #Talen baklänges: 100, 5, 3, 2, 1

regnr=input("Ange regnr:")

print (f"bokstav: {regnr[0:3]}")
print (f"siffra: {regnr[3:6]}")
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
#Tips: Använd slicing och inbyggda funktionen sum().
#Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
   #är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
   #Pröva båda :)
#*numera kan det vara bokstäver i sifferdelen också. Det gör ont att se men det är moderna tider!

#regnr=input("Ange regnr:")

#print (f"bokstav: {regnr[0:3]}")
#print (f"siffra: {regnr[3:6]}")

heltal=input("Ange tal med komma emellan:")
ls=heltal.split(",")

print(f"Första talet: {heltal[0]}")
print(f"Andra talet: {heltal[0]}")
ls2=[]
for elem in ls:
    ls2.append(int(elem))
print(f"Summan av av talen är: {sum(ls2)}")
backwards=", ".join (ls[::-1])
print(f"Talen baklänges: {backwards}")

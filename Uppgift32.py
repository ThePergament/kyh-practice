#"Skriv ett Pythonprogram som tar in en sträng från användaren, och skriver ut följande:
#32.1 Längden på strängen
#32.2 Om strängen är ett "palindrom" eller ej. Exempel på palindrom: rattar, Ebbe. Observera att programmet ska klara att användaren blandar stora och små bokstäver!
#32.3 Utöka programmet så att även uttryck som "Aja Baja" anses vara palindrom, d.v.s filtrera bort alla mellanslag ifrån inputsträngen!
#Tips: använd det vi lärde oss igår kring att vända en sträng och/eller lista baklänges, och join-funktionen. Även list comprehension kan komma till användning."

text =input ("Var god skriv något:")
#print (len(text))
text3 = text.join("")
text2 = text3 [::-1]
if text2.lower() == text3.lower():


    print("Strängen är ett palindrom")
else:
    print("Strängen är inget palindrom, din nöt :P")

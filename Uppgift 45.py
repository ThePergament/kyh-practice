#Uppgift 45!
#Från uppgift1
#print("{}, växte upp i {}. Jag har aldrig programmerat förut.\n"
#"Jag sökte till {} för att det är en säker bransch".format("David Pergament", "Mölndal", "Pvt"))
#Frånuppgift9
'''
import random
def game(number_of_questions,max_value):
    correct_answers = 0
    for i in range(number_of_questions):
        a = random.randint(1,max_value)
        b = random.randint(1,max_value)
        answer = input(f"{a}+{b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

        print ("Du fick, %s + %s rätt."%(correct_answers,number_of_questions))
if __name__ == '__main__':
    number = int(input("Hur många frågor?"))
    max_value = int(input("Ange största tal"))
    game(number,max_value)
'''
#text = input("Lägg till text här:")
#print(f"{text}")
#counter=len(text.split())
#print(str(counter))
#print ("antal ord " + str(counter))

def vowel_counter(char):
    if char.lower() ==  "a" or char.lower() == "i" or char.lower() == "e" or char.lower() == "o" or char.lower() == "u":
        print (char)
        return True
def main():
    counter = 0
    text = input("Ange text:")
    for char in text:
        if vowel_counter(char):
            counter = counter +1
    print(counter)

if __name__ == '__main__':
    main()
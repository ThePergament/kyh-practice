def pwstrength():
    user_answer=input("Ange lösenord:")
    signs ="#%&+_-"
    counter=0

    if len(user_answer) >= 10:
        counter+=1
    for char in user_answer:
        if char in signs:
            counter+=1
            break
    print (counter)
#user_answer = input ().format(s.i)
if __name__ == "__main__":
    pwstrength()

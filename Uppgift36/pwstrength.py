def compute_strength(user_answer):
    #user_answer=input("Ange lösenord:")
    alpha="ABCDEFGHIJKLNMOPQRSTUVXYZ"
    numbers="0123456789"
    signs ="#%&+_-"
    counter=0

    if len(user_answer) >= 10:
        counter+=1
    for char in user_answer:
        if char in signs:
            counter+=1
            #break
        #if char in alpha:
         #   counter+=1
    return counter
#user_answer = input ().format(s.i)
if __name__ == "__main__":
    compute_strength()

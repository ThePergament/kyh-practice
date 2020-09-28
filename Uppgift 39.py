#def add(a,b,c):
#    d= a+b+c
#    return d
#value = add(4, 5, 1)

#if __name__ == "__main__":

    #print(value)
#def add_list(ls):
#    sum=0
#    for i in range(0,5):
#        sum += ls[i]
#   return sum
#numbers=[1,2,3,4,5]
#run = add_list(numbers)
#print(run)


def multiply_list(ls):
    sum=1
    for i in range(0,5):
        sum *= ls[i]
    return sum
numbers=[1,2,3,4,5]
run = multiply_list(numbers)
print(run)

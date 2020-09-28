#def backwards(text):
#    if len(text) <= 1:
#        return text
#
#    return backwards(text[1:]) + text[0]
#run = backwards(text="hoppsan")
#print(run)

def caps(text):
    result=[]
    for c in text:
        if c.isupper():
            result.append(c)
    result1=len(result)
    return result1


run =caps(text="MåNdAg")
print(run)
heltal=input("Ange tal med komma emellan:").split(",")
ls=heltal
ls2 =[int (elem)for elem in ls]

print(f"Första talet: {heltal[0]}")
print(f"Andra talet: {heltal[0]}")
print(f"Summan av av talen är: {sum(ls2)}")
backwards=", ".join (ls[::-1])
print(f"Talen baklänges: {backwards}")
print (f"Udda tal: {heltal[0:100:2]}")
print (f"Jämna tal: {heltal[1:100:2]}")
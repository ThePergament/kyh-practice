import pathlib
p =pathlib.Path('system.log')
#print(p.exists())
loadfile = open(p)
#textline=loadfile.read().splitlines()
#print(textline)
for line in loadfile:
    #fields = line.split
    if 'BEAR' in  line or 'X-RAY' in line:
        print(line)
loadfile.close()


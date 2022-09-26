#file=open("mon27.txt")
#print(file.readlines())
#import re
"""file=open("mon27.txt","r")
for data in file:
    match=re.match("\d+",data)
    if data:
        print(match.group())
"""
import re
with open("mon27.txt",'r') as fo:
    pattern = ('[a-zA-Z]*[0-9_]*@gmail.com*')
    ID=re.findall(pattern,fo.read())
    print(ID)

"""import re
file=open("mon27.txt")
match=re.findall('\d{10}',file)
print(match)
"""
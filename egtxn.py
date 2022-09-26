import re
'''name=open("mailideg")'''
"""with open("kumaresh.txt") as fo:
    patten=('[a-zA-z]+[0-9_]+@gmail.com')
    ID=re.findall(patten,fo.read())
    print(ID)
with open("kumaresh.txt") as ar:
     patten = ('[a-zA-z]*[0-9_]*@gmail.com')
     ID = re.findall(patten,ar.read())
"""
data = "my number is 234-567-890 and 12-34 and 123-456-789"
match=re.findall('\d{3}-\d{3}-\d{3}',data)
print(match)

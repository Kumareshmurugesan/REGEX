import re
"""txt="I'm in love with Priyanka"
x=re.search('^I.*Priyanka$',txt)
if x:
    print("correct  you found it")
else:
    print("you hav'nt  found it")
txt="i love india"
x=re.findall("ia",txt)
print(x)
"""
'''txt="I'm lost in this wolrd"
x=re.search("\w",txt)
print("to show the position:" ,x.start())
'''
'''
txt = "The rain in spain "
x = re.search('\s', txt)
print("No of position: ", x.start())
txt="i love india"
x=re.findall("ia",txt)
print(x)
'''
txt="I'm happy to be alone no body is going to save you be you"
x=re.split('\s',txt,3)
print(x)

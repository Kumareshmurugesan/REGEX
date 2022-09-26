import re

#search the string to see if it starts with "I" and ends with "India"

txt = "I love india"
re.search("^I.*india$",txt)
if txt:
    print("found")
else:
    print("not found")

#findall function returns all occurence

txt = "the rain in spain"
x=re.findall('ai',txt)
print(x)

txt = "The rain in spain"
x = re.findall("india", txt)
print(x)

#The split() function returns a list where the string has been split at each match:

txt = "The rain in spain"
x = re.split('\s', txt)
print(x)

txt = "The rain in spain"
x = re.split('\s', txt,1)
print(x)

#sub function

print(re.sub(r'[a-c]', '&' , 'abcdabcdabcdabcd'))

print(re.sub(r'ac','*','acbdacbdacbdacbd')) #replace if its ac

print(re.sub(r'12','*','123412341234')) # replace number terms

print(re.sub(r'[a-d]','*','abcdghacduiabcdefghacdrgu')) # from to

print(re.sub(r'[a-b][2-4]','*','a1+a2+b4+b3+a6+d4+2a'))

#Meta Character

print(re.sub('h.y','&','hey hai how hey'))

print(re.sub('h.y','&','heey hai how hey'))

print(re.sub('h.y','&','hhy hy hyhy hyyy'))
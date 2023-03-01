import re 

text = input()
x = ("[A-Z]+[a-z]+")
y = re.findall(x , text)

if y:
    print(y)
else:
    print("no matches")
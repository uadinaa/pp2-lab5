import re 

text = input()
x = ("[a-z]+_[a-z]+")
y = re.findall(x , text)

if y:
    print(y)
else:
    print("no matches")
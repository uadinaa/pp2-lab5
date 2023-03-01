import re

text = input()
x = ("(?=[A-Z])")
y = re.split(x, text)
z = " ".join(y)

print(z)



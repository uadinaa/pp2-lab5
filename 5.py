import re 
def ab(text):
    x = ("a.*b$")
    y = re.search(x,text)
    if y !=  None:
        return True 
    return False 

text = input()
z = ab(text)

if z:
    print("matched")
else:
    print("did not match")
    


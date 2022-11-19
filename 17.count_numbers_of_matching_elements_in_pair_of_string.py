a=input("enter first string:")
b=input("enter second string:")
c=list([])
for ch in a:
    if ch in b:
        c.append(ch)

print("number of matching elements:",len(c))
        

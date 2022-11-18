s=input("enter string:")
i=int(input("enter i'th position:"))
s1=""
for j in range(0,len(s)):
    if i!=j:
        s1=s1+s[j]

print("after removing i'th charatcter::",s1)

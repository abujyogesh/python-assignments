s=input("enter number:")
#code for symmetric string
n=len(s)
flag=0
if(n%2)==0:
    i=0
    j=n//2
    while i<n//2 and j<n:
        if s[i]==s[j]:
            i=i+1
            j=j+1
        else:
            flag=1
            break

else:
    flag=1


if(flag==0):
    print("String is symmetric")
else:
    print("String is not symmetric")

#code for palindrom string

i=0
j=n-1
flag=0
while(i<n):
    if s[i]==s[j]:
        i=i+1
        j=j-1
    else:
        flag=1
        break

if(flag==0):
    print("string is palindrome")
else:
    print("string is not palindrom")

            
        
        

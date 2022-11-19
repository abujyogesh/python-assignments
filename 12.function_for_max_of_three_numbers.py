def max(a,b,c):
    if(a>b)&(a>c):
        print("first number is maximum")
    elif(b>c)&(b>a):
        print("second number is maximum")
    else:
        print("third number is maximum")

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

max(a,b,c)

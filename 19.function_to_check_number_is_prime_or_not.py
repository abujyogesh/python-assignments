def prime(n):
    f=0
    for i in range(2,n):
        if (n%i)==0:
            print("number is not prime")
            break
    else:
        print("number is prime")
    


            
n=int(input("enter number::"))
prime(n)


    

    
        

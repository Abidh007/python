num=int (input("enter the number to find factorial"));
face=1;
if(num<0):
    print("sorry,factorial doesnot exist for negative numbers")
elif(num==0):
        
    print("factorial of zero is 1")
    
else:
       for i in range(1,num+1):
           
            fact*=i
print(fact)

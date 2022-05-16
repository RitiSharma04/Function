## Write a function to check if a number is prime or not.


def num(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i+=1
    if count>2:
        print("no")        
    else:
        print("yes")    
a=int(input("enter the num:-"))        
num(a)

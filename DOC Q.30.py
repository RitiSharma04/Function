## Write a function that prints all the prime numbers between 0 and limit where limit is a
##parameter

def limit(a):
    b=[]
    i=1
    while i<a:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count=count+1
            j=j+1
        if count<3:
                b.append(i)
        i=i+1
    print(b)            
a=int(input("enter the number:-"))
limit(a)    



        
        
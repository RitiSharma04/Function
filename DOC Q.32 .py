## Complete the function that takes a non-negative integer n as input, and returns a list of
## all the powers of 2 with the exponent ranging from 0 to n (inclusive).
##n=0 == >[1] #[2^0]
## n = 2 ==> [1, 2, 4] # [2^0, 2^1, 2^2].


def num(a):
    i=0
    b=[]
    while i<=a:
        b.append(2**i)
        i=i+1
    print(b)    
a=int(input("enter the  umber:-"))
num(a)        

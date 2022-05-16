##  Write a Python function to find the Max of three numbers.

def number(a,b,c):
    if a>b and a>c:
        return(a ,"is Maximum number")
    elif b>a and b>c:
        return(b,"is Maximum number")    
    elif c>a and c>b:
        return(c,"is Maximum number")    
a=int(input("enter the number 1:-"))
b=int(input("enter the number 2:-"))
c=int(input("enter the number 3:-"))    
print(number(a,b,c))   
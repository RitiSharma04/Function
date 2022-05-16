## Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print
##“even” if the number is even or and “odd” if the number is odd.

def num(n):
    j=0
    while j<len(b):
        if b[j]%2==0:
            print("even")
        else:
            print("odd")
        j=j+1    
b=[]        
a=int(input("enter the number:-"))        
i=0
while i<a:
    n=int(input("enter the number:-"))
    b.append(n)  
    i=i+1  
print(b)
num(b)            
## Write a Python program to generate and print a list of first and last 5 elements where
##the values are square of numbers between 1 and 30 (both included).
##Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def number(a):
    i=1
    count1=[]
    while i<6:
        count1.append((i**2))
        i=i+1
    print(count1)
    j=a-4
    count2=[]
    while j<=a:
        count2.append((j**2))
        j=j+1
    print(count2)
number(30)    
    

        
        

##Write a function For example, if we give 9119 the function should return 811181, as the square of 9
##is 81 and square of 1 is 1.


def num(a):
    i=0
    while i<len(a):
        print(int(a[i])**2,end="")
        i=i+1
a=input("enter the num:-")
num(a)        





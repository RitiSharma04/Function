## Print multiplication table of 12 using function.
def num(a):
    for i in range(1,11):
        print(a,"x",i,"=",a*i)
a=int(input("enter the number :-"))
num(a)        
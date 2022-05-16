## Part 1

# def add_numbers(number1,number2):
#     print(number1+number2)
# number1=int(input("enter the number1:-"))    
# number2=int(input("enter the number2:-"))
# add_numbers(number1,number2)


## Part 2

def add_numbers_list(list1,list2):
    a=[]
    i=0
    while i<len(list1):
        a.append([list1[i]+list2[i]])
        i=i+1
    print(a)
list1=[2,6,4,6,4]
list2=[3,6,5,4,3]
add_numbers_list(list1,list2)   
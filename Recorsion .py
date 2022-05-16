### fectorial

# def num(a):
#     if a==0:
#         return(1)
#     else:
#         return(a*num(a-1))
# a=int(input("enyter the number:-"))
# print(num(a))

### reverse a string


# def string(a,s):
#     if s==0:
#         print(a[s])
#     else:
#         print(a[s],end="")
#         string(a,s-1)

# a=input("enter the string")
# print(string(a,(len(a)-1)))

### root of a number

# def num(a,b):

#     if b==0:
#         return(1)
#     else:
#         return(a*num(a,b-1))
# a=int(input("enter the num:-"))
# b=int(input("enter the power:-"))
# print(num(a,b))  

###

# a=[3,6,3,6,4,5,5,5,645,43]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)     
     
# def recur_fibo(n):  
#        if n <= 1:  
#            return n  
#        else:  
#            return(recur_fibo(n-1) + recur_fibo(n-2))  
#     # take input from the user  
# nterms = int(input("How many terms? "))  
#     # check if the number of terms is valid  
# if nterms <= 0:  
#        print("Plese enter a positive integer")  
# else:  
#        print("Fibonacci sequence:")  
# for i in range(nterms):  
#        print(recur_fibo(i))  
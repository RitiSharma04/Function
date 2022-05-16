## Write a Python program to print the even numbers from a given list.
##Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
##Expected Result : [2, 4, 6, 8]



def even(*a):
    b=[]
    i=0
    while i<len(a):
        if a[i]%2==0:
            b.append(a[i])
        i=i+1
    return(b)
print(even(1, 2, 3, 4, 5, 6, 7, 8, 9))            
            

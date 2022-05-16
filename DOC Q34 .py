## Q34. Write a function which converts the input string to uppercase.
## Write a function which converts the input string to uppercase.
## For example:-
## [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
## [99, 2, 2, 23, 19] --> 122 (= 99 + 23)
## Input sequence contains minimum two elements and every element is an integer.
def list(*a):
    i=0
    while i<len(a):
        b=a[0]
        if b<a[i]:
            b=a[i]
        i=i+1
    print(b) 
list(10, 14, 2, 23, 19)           
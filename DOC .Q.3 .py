## Write a Python function to sum all the numbers in a list.
## Sample List : (8, 2, 3, 0, 7)
## Output : 20.
 

def  sum(*a):
    i=0
    c=0
    while i<len(a):
        c=c+a[i]
        i=i+1
    return(c)
print(sum(8,2,3,0,7)  )      
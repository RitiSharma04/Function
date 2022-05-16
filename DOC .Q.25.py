## Given a list of numbers, write a Python program to count positive and negative numbers in a List using
## function.
## Example:
## list1 = [2, -7, 5, -64, -14]
## Output: pos = 2, neg = 3
def list(*a):
    i=0
    pos=0
    neg=0
    while i<len(a):
        if a[i]>0:
            pos=pos+1
        else:
            neg=neg+1
        i=i+1
    print(pos)
    print(neg)
list(2, -7, 5, -64, -14)              
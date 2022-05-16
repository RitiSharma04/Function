
def num(*a):
    b=a[0]
    i=0
    while i<len(a):
        if b<a[i]:
            b=a[i]
        i=i+1
    print(b)
num(3,65,3,7,4,67,6,43,3,5,3)


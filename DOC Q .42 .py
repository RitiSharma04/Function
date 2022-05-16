## Find the sum of number digits in List.
##The original list is : [12, 67, 98, 34]
##List Integer Summation : [3, 13, 17, 7]Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
##The original list is : [15, 81, 11, 234]


def list(a):
    i=0
    c=[]
    i=0
    while i<len(a):
        b=a[i]//10
        a[i]=a[i]%10
        c.append(b+a[i])
        i=i+1
    print(c)
a=[12, 67, 98, 34]
list(a)        



    
            


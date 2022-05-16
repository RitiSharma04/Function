# Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of
# consecutive numbers with a difference of one. Print False otherwise.


def list(a):
    b=[]
    i=0
    while i<len(a)-1:
        d=a[i+1]-a[i]
        b.append(d)
        i=i+1  
    print(b)    
    j=0
    count=1
    while j<len(b):
        if b[j]==1:
                count=count+1
        else:
                count=count       
        j=j+1     
    if count==len(b)+1:
            print("TRUE")
    else:
            print("FALSE")        
a=[-3 ,-2, -1, 0, 1]    
list(a)        






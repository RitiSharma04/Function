## Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of
## consecutive numbers with any constant difference between numbers. Print False otherwise.

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
a=[]
d=int(input("enter the number:-"))
h=0
while h<=d:
    e=int(input("enter the number:-"))
    a.append(e)
    h=h+1
list(a)        








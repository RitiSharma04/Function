def list(a):
    b=[]
    c=[]
    product=0
    sum=0
    i=0
    while i<len(a):
       if a[i]> 1:
        
           
        for j in range(2,a[i]):
            if (a[i] % j) == 0:
                b.append(a[i])
                product=product+a[i]

                break
        else:
                c.append(a[i])
                sum=sum+a[i]
        i=i+1   
    print("product of non prime number:-",product)
    print("sum of prime number:-",sum)   
          
a=[67,97,8,5,12,5,3,45]           
list(a)  


                  

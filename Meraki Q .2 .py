def perfect(a):
    count1=0
    i=1
    while i<=a:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count=count+j
            j=j+1
        if i==count:
            count1=count1+i
        i=i+1   
        print(count1)   

perfect(1000) 






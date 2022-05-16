def number(a):
    count=0
    i=0
    while i<=a:
        if i%3==0 or i%5==0:
            count=count+i
        i=i+1    
    print(count)    
number(10)
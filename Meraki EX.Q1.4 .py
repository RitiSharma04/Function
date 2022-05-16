def reverse_list(*a):
    b=a[0]
    i=0
    while i<len(a):
        if b>a[i]:
           b=a[i]
        i=i+1
    print(b)
reverse_list(8, 6, 4, 8, 4, 50, 2, 7)



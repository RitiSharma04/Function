def strings(a,b):
    if len(a)>len(b):
        print(len(a),a)
    elif  len(a)==len(b):
        print(a)
        print(b)
    else:
        print(len(b),b)
a=input("enter the strings 1")
b=input("enter the strings 2")      
strings(a,b)      


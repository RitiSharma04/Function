def speed(a):
    point=0
    if a<70:
        print(70)
    elif  a>70:
        point=((a-70)/5)*1
        print(point)
        if  point>12:
            print("License suspended")
a=int(input("enter the speed:-"))            
speed(a)            
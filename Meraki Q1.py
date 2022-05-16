def eligible(name,age):
    if age>=18:
        return(name,"is eligible for voting")
    else:
        return(name,"is not eligible for voting")
name=input("enter  the name")            
age=int(input("enter the age:-"))
print(eligible(name,age))
## Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting
##to be 18. )


def voting_ableity(name,age):
    if age>=18:
        print(name,"is able to give vote")
    else:
        print(name,"is not able to give vote")
name=input("enter the name:-")
age=int(input("enter the age:-"))  
voting_ableity(name,age)          
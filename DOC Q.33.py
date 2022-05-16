## Write function bmi that calculates body mass index (bmi = weight / height2).
## if bmi > 30 return "Obese"
## if bmi <= 18.5 return "Underweight"
## if bmi <= 25.0 return "Normal"
## if bmi <= 30.0 return "Overweight"
def body_mass(weight,height):
    if (weight/height)*2>30:
        print("Obese")
    elif (weight/height)*2<=18.5:
        print("Underweight") 
    elif(weight/height)*2<25.0:
        print("Normal")
    elif (weight/height)*2<=30.0:
        print("Overweight") 
weight=int(input("enter the weight:-"))
height=int(input("enter the height:-"))
body_mass(weight,height)           



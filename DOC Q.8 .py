##Write a Python function that accepts a string and calculate the number of upper case letters and
##Sample String : 'The quick Brow Fox'
##Expected Output :
##No. of Uppercase characters : 3
##No. of Lower case Characters : 12

def string(a):
    i=0
    upper_case=0
    lower_case=0
    while i<len(a):
        if a[i]>="A"and a[i]<="Z":
            upper_case=upper_case+1
        elif a[i]>="a"and a[i]<="z":
            lower_case=lower_case+1
        i=i+1
    print(upper_case)
    print(lower_case)
string("The quick Brow Fox")   
          
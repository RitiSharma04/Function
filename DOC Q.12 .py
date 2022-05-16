## .Numbers ending with zeros are boring.
##They might be fun in your world, but not here.
##Get rid of them. Only the ending ones.
##1450 -> 145
##960000 -> 96
##1050 -> 105
##-1050 -> -105

def num(a):
    i=len(a)
    while i>0:
        if a[i]==0:
            continue
        if a[i]>="1" and a[i]<"9":
            print(a[i],end="")
        i=i-1
num("1450")            

    
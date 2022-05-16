##Write a Python program to find the list with maximum and minimum length.
##Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
##List with maximum length of lists:
##(3, [13, 15, 17])
##List with minimum length of lists:
##(1, [0])

a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

i=0
b=len([0])
c=len([0])
while i<len(a):
    if b<len(a[i]):
        b=len(a[i])
    if c>len(a[i]):
        c=len(a[i])
    i=i+1
print(b)
print(c)           

print(len(a[i]),b )
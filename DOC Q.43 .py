## Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from
##the user.
##ample Input:
## 1
##Sample Output:
##q
##Sample Input:
##3
##Sample Output:
##5
##b
##q

def list(a):
    b=int(input("enter the num:-"))
    i=b
    while  i>=1:
        print(a[-i])
        i=i-1
a=["a", 1,"2", 5, "b", "q"]     
list(a)   



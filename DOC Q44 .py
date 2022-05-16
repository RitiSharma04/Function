# Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b
# Sample Input:
# 3
# Sample Output:
# q
# b
# 5

def list(a):
    b=int(input("enter the indexing you want:-"))
    i=1
    while i<=b:
        print(a[-i])
        i=i+1
a=["a", 1,"2", 5, "b", "q"]    
list(a)

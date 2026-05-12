'''

***
**
*

'''

def patetrn(n):
    if(n==0):
        return
    print("*" * n)
    patetrn(n-1)


print(patetrn(5))
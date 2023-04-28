a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
temp=0
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("swaping number a and b" ,a,b)
swap(a,b)

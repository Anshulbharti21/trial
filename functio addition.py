a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=float(input("enter 3rd number"))
def grater(a,b,c):
    if(a>b and a>c):
        print("a is grater",a)
    elif(b>c and b>a):
        print("b is grater",b)
    elif(c>a and c>b):
        print("c is grater",c)
    
grater(a,b,c)

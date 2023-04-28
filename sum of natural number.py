num=int(input("enter the number hear :"))
if(num<0):
    print("please enter the valid number ")
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1
    print(sum)


num=int(input("enter the number you wont sum :"))
sum=0
for i in range(0,num):
    sum+=i
    print("sum of all natural number is :",sum)

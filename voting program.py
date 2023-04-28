'''a=int(input("enter input "))
if(a<18):
    print("you are under age",a)
elif(a>18):
    print("you are eligible for voting",a)
else:
    print("invalid input")'''

    
country = int(input("enter your country \n press 1 for india \n press 2 for america \n press 3 for nepal\n press 4 for australia"))
if(country == 1):
    print("congratulation you have indian nationality")
    state=int(input("enter your state \n press 5 for himachal pradesh \n press 6 for punjab \n press 7 for jamu kashimer \n press 8 for goa"))
    if(state == 5):
             print("congratulation you are  from himachali you have to vist punjab ,jamu kashimer,goa")
    elif(state == 6):
             print("congratulation you are from punjabi you have to vist himachal ,jamu kashimer,goa")
    elif(state == 7):
             print("congratulation you are from jamukashmir you have to vist himachal ,punjab,goa")
    elif(state == 8):
             print("congratulation you are from goa you have to vist himachal ,jamu kashimer,punjab")
    else:
        print("plzz enter valid input")
        
elif(country == 2):
    print("congratulation you have america nationality")
    state=int(input("enter your state \n press 9 for Arkansas \n press 10 for california \n press 11 for colorado \n press 12 for alaska"))
    if(state == 9):
             print("congratulation you are from arkanss you have to vist california ,colorado,alaska")
    elif(state == 10):
             print("congratulation you are  fromcalifornia you have to vist arkanss,colorado,alaska")
    elif(state == 11):
             print("congratulation you are  from colorado you have to vist california, arkanss,alaska")
    elif(state == 12):
             print("congratulation you are from alaska you have to vist california, arkanss, colorado")
    else:
        print("plzz enter valid input")
elif(country == 3):
    print("congratulation you have nepal nationality")
    state=int(input("enter your state \n press 1 for madhesh pradesh \n press 2 for bagmati pradesh  \n press 3 for gadaki pradesh \n press 4 for lumbini pradesh"))
    if(state == 1):
             print("congratulation you are from madhesh pradesh you have to vist bagmati pradesh  ,gandaki pradesh ,lumbini pradesh")
    elif(state == 2):
             print("congratulation you are from bagmati pradesh you have to vist gandaki pradesh ,lumbini pradesh ,madhesh pradesh")
    elif(state == 3):
             print("congratulation you are from gandaki pradesh you have to vist lumbini pradesh, madhesh pradesh, bagmati pradesh")
    elif(state == 4):
             print("congratulation you are from lumbini pradesh you have to vist gandaki pradesh, bagmiti pradesh,madesh pradesh")
    else:
        print("plzz enter valid input")
elif(country ==4):
    print("congratulation you have australian nationality")
    state=int(input("enter your state \n press 1 for queensland \n press 2 for western australia  \n press 3 for south australia \n press 4 for tasminia"))
    if(state == 1):
             print("congratulation you are from queesland you have to vist western australia  ,south australia ,tasminia")
    elif(state == 2):
             print("congratulation you are from western australia you have to vist south australia ,tasminia ,queensaland")
    elif(state == 3):
             print("congratulation you are from south australia you have to vist tasminia, queensaland, western australia")
    elif(state == 4):
             print("congratulation you are from tasminia you have to vist queensaland, western australia,south australia")
    else:
        print("plzz enter valid input")
    

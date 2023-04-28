a={5,10,15,20,25}
b={3,4,5,99}
#print(type(a))
b.pop()#random item delete krta h
print(b)
a.remove(25)#remove the value
print(a)
print(a.symmetric_difference(b))
a.update({6,58,86})#it will update the values in a 
print(a)
print(a.union(b))#it will unite a and b values
print(a.issuperset(b))
print(a.issubset(a))
a.add(555555)
print(a)
print(a.difference(b))
a.difference_update(b)
a.discard(56)#it is used to remove the value if exist else it will not going to show you the error

import array as ar
a=ar.array('i',[1,2,3,4])
print(a)
print()
print("Acessing elements of array")
print(a[0])
print(a[-1])
a[0]=9
print(a)
a[1:3]=ar.array('i',[8,7])
print(a)
a.append(6)
print(a)
a.extend([5,4,3]) # add multiple element
print(a)
del a[2]
print(a)
a.remove(4) #no or value to remove
print(a)
a.pop(2) #index 
print(a)

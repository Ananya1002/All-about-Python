import os

#sliping in indexes
name="ananya"
a=name[1:6:2]
print(a)

#functions
a="my name is ananya"
print(len(a))
print(a.count("my"))
print(a.endswith("ya"))
print(a.capitalize())
print(a.find("t"))

#lists
a=[1,2,3,4]
a[0]=23
print(a[2])

#list slicing
frds=["ananya","ana","anua","uatdd"]
print(frds[1:4])
print(frds[-4:])


#list methods
l1=[1,8,7,2,21,15]
l1.sort()
l1.reverse()
l1.append(9)
l1.insert(2,7)
l1.pop(2)
print(l1)


#tuples
a=(1,)
a[0]=4 #which  proves cant be modified
print(a)


#tuples methods
t1=(1,7,2,7)
print(t1.count(7))
print(t1.index(2))
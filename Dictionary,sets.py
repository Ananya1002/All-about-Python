import os

#Dictionary
a={
    "a":"ananya",
    "g":"ghgnh",
    "as":[1,2,3]
}
print(a['as'])

#nested dict
a={
    "m":{"a":"ananya"}
}
print(a['m']['a'])


#dictionary methods
a={
    "a":"ananya",
    "g":"ghgnh",
    "as":[1,2,3],
    1:2
}
print(list(a.keys()))
print(a.values())
print(a.items())
print(a.get("a"))
print(a)


#Sets
a={1,2,3}
print(a)
print(type(a))


#empty set
a=set()
a.add(1)
a.add(2)
a.add(1) # it will be added ony 1 time only
a.add((3,4,5))
print(a)
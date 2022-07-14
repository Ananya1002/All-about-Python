import os

print("hello world")


#variable
a="ananya"
print(a)
print(type(a))


#operators
a=12
a+=2
b=8
print("the value of a+b =",12+8)
print("the value of a*b =",12*8)
print(a)
b=(2>9)
print(b)


#logical operators
bool1=True
bool2=False
print("the value of bool1 and bool2 is ",(bool1 and bool2))
print("the value of bool1 and bool2 is ",(not bool2))
print("the value of bool1 or bool2 is ",(bool1 or bool2))


#to convert string in int
a="123"
a=int(a)
print(a+9)
print(type(a))
'''
'''
#ques 
a=input("enter first number")
b=input("enter second number")
a=int(a)
b=int(b)
avg=(a+b)/2
print("avg of two numbers is", avg)

#ques
a=input("enter a number")
a=int(a)
print(a*a)

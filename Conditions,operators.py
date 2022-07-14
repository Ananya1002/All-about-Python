import os

#if else condition 1
a=43 # hamesha pehle walli statment hi exicute hogi agr vo false hoti h to hi next padhi jayegi 
if(a<30):
    print("True")
elif(a>50):
    print("Less than 50")
else:
    print("False")
print("Done")


#relational operators
age=int(input("Enter your age: "))
if age>18:
    print("Yes")
else:
    print("No")


#logical operatiors(AND)
age=45
if(age>10 and age<50):
    print("Yes")
else:
    print("No")


#logical operators(OR)
age=45
if(age>50 or age<30):
    print("Yes")
else:
    print("No")


#if else clause
a=7
if (a==1):
    print("Yes")
elif(a<10):
    print("No")
else:
    print("optional")
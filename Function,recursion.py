from ast import Return
import os

def my_sum(num1,num2):
    return num1 +num2
s=my_sum(1,2)
print(s)

def greet(name="Stranger"): #default parameter value
    print("Good morning! "+name)
greet("Ananya")
greet()


#recursion(using for)
n=4
product=1
for i in range(n):
    product=product * (i+1) # by default i ki range 0 to 3 hogi
print(product)


#recusion(using function)
def factorial_iter(n):
    product=1
    for i in range(n):
        product=product * (i+1) 
    return product
print(factorial_iter(5))

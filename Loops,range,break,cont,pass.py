import os

#while loop

i=4
while i<10:
    print("Yes" +str(i))
    i=i+1
print("Done")

i=1
while i<=50:
    print(i)
    i=i+1


#for loop 
names=('ananya','ana','sub','hon')
for people in names:
    print(people)


#range
for i in range(1,8,2):#(start,stop,step size)
    print(i)


#for with else
for i in range(1,8,2):
    print(i)
else:
    print("Done")


#break
for i in range(1,8):
    print(i)
    if i==5:
        break
else:
    print("Done")


#continue
for i in range(1,8):
    if i==5:
        continue # jahan cont h vo vaule ko chodke print hoga output
    print(i)


#pass
i=4
if i<10:
    pass #to do nothing 
print("Done")


#question
num=int(input("Enter a number:"))
prime=True
for i in range(2,num):
    if(num%1==0):
        prime=False
        break
if prime:
    print("The number is prime!")
else:
    print("The number is not prime!")
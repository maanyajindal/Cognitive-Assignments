#q1
print('anything cool')

#q2.1
a=2
b=2
c=a+b
print(c)

#2.2
a='Manya'
b='Jindal'
c=a+b
print(c)

#2.3
a='2'
b='maths'
print(a+' '+b)

#3.1
a=int(input('enter no.'))
if(a==0):
    print('it is zero')
elif(a<0):
    print('it is negative')
else:
    print("it is positive")  

#3.2
a=int(input('enter no.'))  
if(a%2==0):
    print("even no")
else:
    print("odd no")  

#4.1
for i in range(1,11):
    print (i)  

#4.2
i=1
while(i<11):
    print (i) 
    i=i+1 

#4.3
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)    

#5.1
mylist=[1,2,3,4,5]
print(max(mylist),min(mylist))

#5.2
dict = {
  "name": "Farah",
  "class": "7",
  "sub": 'eng'
}
print(dict["sub"])

#5.3
mylist = [3, 1, 4, 5, 9, 2, 6, 3, 5]
mylist.sort()
print("ascending order:",mylist)
mylist.sort(reverse=True)
print("descending order:",mylist)

#5.4
dict1 = {
  "name": "Farah",
  "class": "7",
  "sub": 'eng'
}
dict2 ={
    'a':1,'b':2
}
merge=dict1 | dict2
print('after merging',merge)

#6.1
s=input('give your input:')
count=0
for vowel in s:
    if(vowel=='a' or vowel=='e' or vowel=='i' or vowel=='o' or vowel=='u'):
        count=count+1
print(count)  

#6.2
s=input('give your input:')
print(s[::-1])

#6.3
s=input('give your input:')
n=s[::-1]
if(s==n):
    print("yes palindrome")
else:
    print("not palindrome")   

#7.1

f=open("maths.txt","w")
f.write("thank you")
f.close()
f=open("maths.txt","r")
print(f.read())
f.close()    


7.2
f=open("maths.txt","a")
f.write("its ok\n")
f.write("smile please")
f.close()
f=open("maths.txt","r")
print(f.read())
f.close()

#7.3
f=open("maths.txt","r")
filelines=f.readlines()
count=0
for line in filelines:
    count=count+1
print(count) 
f.close() 

#8.1
try:
    n=4
    d=0
    r=n/d
    print(r)
except ZeroDivisionError:
    print("error")


#8.2
try:
    a=int(input("Enter no:"))
except ValueError:
    print("invalid input")

#8.3
try:
    a=int(input("enter no"))
except ValueError:
    print("invalid input")
finally :
    print("code will executed")        


#9.1
import random
i=1
while(i<=5):
    print(random.randrange(1,100))
    i=i+1

#9.2
import random
a=random.randrange(1,100)
print(a)
flag=True
for i in range(2,a-1):
    if(a%i==0):
        flag=False
if(flag==True):
    print("it is prime")
else:
    print("not prime")         

#9.3
import random
a=random.randrange(1,7)
print (a)

#9.4

import random
list=[1,3,5,7,9,2]
random.shuffle(list)
print(list)


#9.5
import random
list=[1,3,5,7,9,2]
print(random.choice(list))

#9.6
import string
import random
length=7

password=''.join(random.choices(string.ascii_letters+string.digits,k=7))
print(password)

#9.7
import random

card=random.choice(['spades','heart','diamond','club'])
number=random.choice([2,3,4,5,6,7,8,9,10,'ace','jack','queen','king'])
print(str(number)+ "of"+ card)

#10
import sys
sys.argv=['sum','2','3','maths']
n1=float(sys.argv[1])
n2=float(sys.argv[2])


#11.1
import math
a=math.sqrt(49)
print(a)

#11.2
import datetime
a=datetime.datetime.now()
print(a)

#11.3
import os
print(os.listdir())
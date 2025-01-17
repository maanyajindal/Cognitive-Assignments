#1
list=[10,20,30,40,50,60,70,80]
list.append(200)
list.append(300)
print(list)
list.remove(10)
list.remove(30)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#2
tuple= (45, 89.5, 76, 45.4, 89, 92, 58, 45)
a=max(tuple)
print(a)
print(tuple.index(a))

b=min(tuple)
print(b)
print(tuple.count(b))

reverse=tuple[::-1]
l=list(reverse)
print(l)

flag=False
for i in tuple:
    if(i==76):
        flag=True
        break
if(flag):
    print("index of element is:",tuple.index(i))
else:
    print("element is not present")   

#3  
#   All odd numbers 
import random
i=0
l=[]
while(i<100):
    r=random.randrange(100,900)
    l.append(r)
    i=i+1
count=0
for value in l:
    if(value%2 !=0):
        count=count+1
        print(value)    
print(" count is" ,count)

#All even numbers
count1=0
for value in l:
    if(value%2 ==0):
        count1=count1+1
        print(value)    
print(" count1 is" ,count1)

#All prime numbers
import random
i=0
l=[]
while(i<100):
    r=random.randrange(100,900)
    l.append(r)
    i=i+1
count2=0
flag=True
for i in range(2,value):
    if(value%i==0):
        flag=False
if(flag==True):
    print("it is prime")
else:
    print("not prime")

#4
#union
a = {34, 56, 78, 90}  
b = {78, 45, 90, 23} 
c= a.union(b)
print(c)
#intersection
d=a.intersection(b)
print(d)
#symmetric difference
e=a.symmetric_difference(b)
print(e)
#subset suoerset
print(a.issubset(b))
print(b.issuperset(a))
#remove score x
x=int(input("enter no"))
flag =False
for k in a:
    if(k==x):
        temp=True
        break
if(temp==True):
    a.remove(x)
    print(a)
else:
    print("not present")    

#5
dict={
    "name":"kely",
    "age": 25,
    "salary": 8000,
    "city": "new york"
}        
dict["location"]=dict.pop("city")
print("updated:",dict)
print("Add through dot format method")
print()
a=float(input("first digit"))
q=int(input("2nd digit"))
summ=a+q
print("sum of{0} addd {1} is {2}".format(a,q,summ))
print()
print("area of triangle")
w=int(input("enter irst side"))
e=int(input("enter secod side"))
r=int(input("enter third side"))
s=(w+e+r)/2
area=(s*(s-w)*(s-e)*(s-r))**0.5
print("area is %0.2f"%area)
print()
print("square root")
import cmath
t=int(input("enter first no "))
y=int(input("enter secod no"))
u=int(input("enter third no"))
d=(y**2)-4*t*u
root1=(-y+cmath.sqrt(d))/(2*t)
root2=(-y-cmath.sqrt(d))/(2*t)
print(root1,root2)
print()
print("Swapping 2 no with or without extra var")
print("swap using temp var")
u=3
i=4
print(u,i)
temp=u
u=i
i=temp
print(u,i)
print("Now swap using only given var")
print()
print(u,i)
u=u+i
i=u-i
u=u-i
print(u,i)
print()
print("random no priting")
print()
import random
print(random.randint(0,56))
print()
print("kilo to miles")
print()
kilo=float(input("enter "))
convfact=0.62137
miles=kilo * convfact
print("miles is ",miles)           
           
print()
print("celcius to fahrenheit")
print()
cel=float(input("enter"))
fahren=(cel*1.8)+32
print("%0.1f celcius is equal to %0.1f fahrenheit"%(cel,fahren))
print()
print("print Calender")
print()
import calendar
g=int(input("enter year"))
h=int(input("enter month"))
print(calendar.month(g,h))
print(calendar.prcal(2020))

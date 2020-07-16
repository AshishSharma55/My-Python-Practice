print("check weather entered no is positive negative or zero")
print()
n=int(input("enter the no to check"))
if n==0:
    print("enter no  is zero")
elif n<0:
    print("enter no {0} is negative".format(n))
else:
    print("enter no {0} is positive".format(n))
print()
print("Check the entered no is odd or even")
print()
a=int(input("enetr the no to check"))
if a%2==0:
    print("enter no {0} is even".format(a))
else:
    print("enetred no {0} is odd".format(a))
print()
print("check weather the entered year is leap or not")
q=int(input("enter the year"))
if q%4==0:
    if q%100==0:
        if q%400==0:
            print("{0} is leap year".format(q))
        else:
            print("{0} is not a leap year".format(q))
    else:
         print("{0} is  a leap year".format(q))
else:
     print("{0} is not a leap year".format(q))
print()
print("To check weather entered no is prime or not")
print()
w=int(input("enter no to check"))
if w>1:
    for i in range(2,w):
        if w%i==0:
            print("{0} is not prime".format(w))
            break
    else:
        print("{0} is prime".format(w))
else:
    print("not prime")
print()
print("Print all Prime no between a specified range")
print()
lower=int(input("enter lower range"))
upper=int(input("enter upper range"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                
                break
        else:
            print(num)
print()
print("Find factorial of the number")
print()
no=int(input("enter the no"))
fact=1
if no<0:
    print("no factorial exist for negative no")
elif no==0:
    print(" fact of zero is 1")
else:
    for i in range(1,no+1):
        fact=fact*i
    print("factorial is",fact)
print()
print("printing table of the given no")
print()
t=int(input("enter the table no"))
i=1
while i<=10:
    print(t,"*",i,"=",t*i)
    i=i+1
print()
print("Printing Fibonacciii series")
print()
terms=int(input("enter upto which u want to print"))
f=0
s=1
for j in range(0,terms):
    print(f)
    temp=f
    f=s
    s=temp+s
print()
print("Without third variable")
print()
nterms=int(input("enter no upto to which u want to print"))
n1=0
n2=1
count=2
if nterms<=0:
    print("no series for this")
elif nterms==1:
    print(n1)
else:
    print(n1,",",n2,end=',')
    while count < nterms:
        nth =n1+n2
        print(nth,end=',')
        n1=n2
        n2=nth
        count+=1
    
print()
print("Sum of number")
l=int(input("enter the no"))
sum=0
while l>0:
    sum+=l
    l-=1
print(sum)    

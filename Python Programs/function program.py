print()
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("enter first"))
num2=int(input("enter second"))
print("The lcm of no is ",lcm(num1,num2))
print()
print("Finding hcf of no")
print()
def hcf(q,w):
    if q>w:
        smaller=w
    else:
        smaller=q
    for i in range(1,smaller+1):
        if((q%i==0) and (w%i==0)):
            hcf=i
    return hcf
numm1=int(input("enter no for hcf"))
numm2=int(input("enter no for hcf"))
print("hcf os no is",hcf(numm1,numm2))
print()
print("LCM hcf using formula")
print()
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)/gcd(a,b)
a=8
b=12
print("lcm and hcf of no is {0} and {1} ".format(lcm(a,b),gcd(a,b)))
print()
print("converting deci to binary")
def decitobin(nummm):
    if nummm>1:
        decitobin(nummm//2)
    print(nummm%2,end='')
if __name__=='__main__':
    deci=17
    decitobin(deci)
print()
print("Printing Fact using Reccursion func")
print()
def recfact(p):
    if p<0:
        print("emter positive")
    elif p==0:
        return 1

    else:
        return (p*recfact(p-1))
print("the fact of the no is",recfact(5))
print()
print("Fibonacii series using recursion")
print()
def recfibo(g):
    if g <= 1:
        return g
    else:
        return (recfibo(g-1) + recfibo(g-2))
terms=int(input("enter upto u want series"))
if terms<=0:
    print("enter positive")
else:    
    for i in range(terms):
        print(recfibo(i))

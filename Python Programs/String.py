print("Sorting letters or words or alphabat")
s=input("enter the string")
a=s.split()#first we split them to know the worls or letters
print(a)
a.sort() #then we sort them
print(a)
for i in a:
    print(i)
print()
print("Check string is palindrome or not using reversed func")
str="Amma" 
str=str.casefold()
print(str)
r=reversed(str)

if list(r)==list(str):
    print("its pallindrome string")
else:
    print("not")
print()
print("Palindrom without using reversed func")
q="mam"
o=q[::-1]
if q==o:
    print("yes its palindrome")
else:
    print("its not")
    
print()
print("reverse both part of string")
a=input("enter")

list = a.split()
c= list[0][::-1]
d= list[1][::-1]
e=c + ' '   + d
print(e)
print()
print("reverse half part of string")
a=input("enter")

list = a.split()
c=list[0]
d= list[1][::-1]
e=c + ' '   + d
print(e)
print()
print("counting no of letters")
letters ="aAbBcCdD"
s=input("enter ")
count={}.fromkeys(letters,0)
for char in s:
    if char in count:
        count[char]+=1
print(count)        
print()
print(" remove punctuation from string")
punct="'''[]{};:,./<>=\'''"
non_punc=" "
s=input("enter")

for char in s:
    if char not in punct:
        non_punc=non_punc+char
print(non_punc)





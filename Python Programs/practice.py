punct="'''[]{};:,./<>=\'''"
non_punc=" "
s=input("enter")

for char in s:
    if char not in punct:
        non_punc=non_punc+char
print(non_punc)


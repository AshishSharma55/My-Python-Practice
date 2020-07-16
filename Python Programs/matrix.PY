a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print("first row is",a[0])
print("Third element of 2nd row",a[1][2])
column=[]
for row in a:
    column.append(row[2])
print("Third column is",column)    
print()
print("Mutliplication of matrix")
b=[[1,2],
   [3,4]]
c=[[5,6],
   [7,8]]
r=[[0,0],
   [0,0]]
for i in range(len(b)): #iterate through row of b
    for j in range(len(c[0])): #iterate through column of c
        for k in range(len(c)): #iterate through row of c
            r[i][j]+=b[i][k]*c[k][j]
for result in r:
    print(result)
print()
print("Transpose") #using list comprehension
s=[[1,2,3],
   [4,5,6]]
results= [[a[j][i] for j in range(len(s))] for i in range(len(s[0]))]
for t in results:
           print(t)
print()
print("Transpose using normal formula")
re=[[0,0],
    [0,0],
    [0,0]]
for i in range(len(s[0])):
    for j in range(len(s)):
        re[i][j]=s[j][i]
for trans in re:
    print(trans)

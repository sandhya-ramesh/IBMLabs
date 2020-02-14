R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

a= []
b=[]
c=[]
for i in range(R):
    for j in range(C):
        x=int(input("Enter the element"))
        a.append(x)
    b.append(a)
    a=[]
for i in range(R):
    for j in range(C):
        x=int(input("Enter the element"))
        a.append(x)
    c.append(a)
    a=[]
for i in range(R):
    for j in range(C):
        print(b[i][j]+c[i][j])


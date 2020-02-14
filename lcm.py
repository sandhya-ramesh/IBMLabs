def compute_lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
x=int(input("Enter the first value"))
y=int(input("Enter the second value"))
print("The lcm of",x,"and" ,y,"is",compute_lcm(x,y))
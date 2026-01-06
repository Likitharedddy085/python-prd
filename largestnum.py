a=input()
X,Y,Z=a.split(",")
num1=int(X)
num2=int(Y)
num3=int(Z)
great=0
if num1>num2:
    if num1>num3:
        great=num1
    else:
        great=num3
elif num2>num1:
    if num2>num3:
        great=num2             
    else:
        great=num3
elif num3>num1:
    if num3>num2:
       great=num3
    else:
        great=num2
print(f"the largest numbers is {great}")


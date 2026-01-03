num1=int(input("Give 1st number:"))
num2=int(input("Give 2nd number:"))
operator=input("Give operator")
if operator=='+':
    print(f"Addition of 2 numbers is {num1+num2}")
elif operator=='-':
    print(f"subtraction of 2 numbers is {num1-num2}")
elif operator=='*':
    print(f"Multiplication of 2 numbers is {num1*num2}")
else:
    print(f"Division of 2 numbers is {num1/num2}")
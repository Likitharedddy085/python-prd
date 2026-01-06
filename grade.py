m=int(input("marks in math:"))
s=int(input("marks in science:"))
e=int(input("marks in english:"))
total_marks=m+e+s
average=total_marks/3
percentage=(total_marks/300)*100
grade=""
if percentage>90:
    grade="A"
elif percentage>80 and percentage<=90:
    grade="B"
elif percentage>70 and percentage <=80:
    grade="C"
else:
    grade="p"
print(f"Total marks:{total_marks} \nAverage marks:{average} \n Grade:{grade}")
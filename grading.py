#takeinput
def takein():
    name=str(input("enter your name: "))
    mark1=int(input("enter your marks of science: "))
    mark2=int(input("enter your marks of thermal: "))
    mark3=int(input("enter your marks of math: "))
    
    total=mark1+mark2+mark3
    average_marks=total/3
    if average_marks>=80:
        grade='A'
    elif 60<=average_marks<80:
        grade='B' 
    elif 40<=average_marks<60:
        grade='C' 
    elif average_marks<40:
        grade='F' 
    else:
        print("please retry again:")

    print(f"Your name is {name},your total marks is {total},your average marks is {average_marks} and your grade is {grade} ")

takein()
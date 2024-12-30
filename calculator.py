## Basic Calculator ## 

#input section
num1=int(input('enter the first number:'))
num2=int(input('enter the second number: '))

#display section
print("for operation selection:")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.modulus")

#function definition
def add_op(num1,num2):
    result=num1+num2
    print("addition is:",result)
def sub_op(num1,num2):
    result=num1-num2
    print("substraction is:",result)
def multi_op(num1,num2):
    result=num1*num2
    print("multiplication is:",result)
def div_op(num1,num2):
    if num2!=0:
        result=num1/num2
        print("division is:",result)
    else:
        print("division by zero is not allowed.")
def mod_op(num1,num2):
    result=num1%num2
    print("remainder is:",result)


#function call + looping
selection=int(input('enter the operation:'))
if selection==1:
    add_op(num1,num2)
elif selection==2:
    sub_op(num1,num2)
elif selection==3:
    multi_op(num1,num2)
elif selection==4:
    div_op(num1,num2)
elif selection==5:
    mod_op(num1,num2)
else:
    print("please enter valid number")
#input
p=int(input("enter your principle amount:"))
r=int(input("enter ypur interest rate:"))
t=int(input("enter the time period in years:"))

def si():
    smpi=p*t*r/100
    print("your interest amount is: ",smpi)
    ta=p+smpi
    print("your total amount is going to be: ",ta)

si()

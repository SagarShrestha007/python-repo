#takeinput
num=int(input("enter a number: "))
#check positive-negative
def posneg():
    if num>0:
        print("your number is positive",)
    elif num<0:
        print("your number is negative",)
    else:
        print("please renter a natural number")
#check even-odd
def evenodd():
    if num%2==0:
        print("your number is even")
    else:
        print("your number is odd")

posneg()
evenodd()

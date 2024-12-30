#def
def fact(n):
    if n==1 or n==0:
        print(f"your factorial of {n}! is: 1")
    else:
        factorial=1
        for i in range(1,n+1):
            factorial*=i
            print(f"factorial of {n}! is :{factorial}")
#input
n=int(input("enter the number you want factorial of:"))
fact(n)

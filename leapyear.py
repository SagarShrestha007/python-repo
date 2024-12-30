#inut
num=int(input("enter the number you want to check"))

def lpyear(num):
    if (num%4==0 and num%100!=0) or (num%400==0):
       return True
    else:
       return False
if lpyear(num):
    print(f"{num} is leap year.")
else:
    print(f"{num} is not leap year")

#input
age_in=int(input("enter your age: "))
income_in=int(input("enter your income : "))

#defn 
def checkage():
    if age_in<60 and age_in >=18:
        result='eligible'
    else:
        result='not eligible'
    print(f"based on age you are {result}")
def checkincome():
    if income_in>30000 or income_in==30000:
        result1='eligible'
    else:
        result1='not eligible'
    print(f"based on income you are {result1}")
#call
checkage()
checkincome()

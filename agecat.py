#defn
def age_check(agein):
    if agein <13:
        print(f"you are an child as your age is {agein}")
    elif 13<=agein<=19:
        print(f"you are an teenager as your age is {agein}")
    elif 20<=agein<=59:
        print(f"you are an adult as your age is {agein}")
    elif agein>=60:
        print(f"you are an senior as you age is {agein}")
    else:
        print("please enter a valid number :")
#input
agein=int(input("enter your age"))
age_check(agein)

#multiplication table
#fun defn
def mul():
    print(f"multiplication table of {num}:")
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
#input from user
num=int(input("enter any number that you eant multiplication table of: "))        

mul()
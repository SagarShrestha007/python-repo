#fun defn
def even_check(num):
    if num%2==0:
        print(f" your number {num} is even")
    else:
        print(f"your number {num} is odd")


#input
start=int(input("eneter a number"))
end=int(input("enter a number"))

print("even number between {start} and {end} are:")
for num in range(start,end+1):   
    even_check(num)
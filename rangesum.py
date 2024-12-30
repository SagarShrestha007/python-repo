#input
start=int(input("enter your starting number: "))
end=int(input("enter your ending number: "))
sum=0
count=0
for nums in range(start,end+1):
     sum+=nums
     if nums%3==0:
          count+=1
print("sum is:",sum)
print("count is :",count)
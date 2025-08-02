n=int(input("Enter the number:"))
order=len(str(n))
sum=0
k=n
while(n>0):
    r=n%10
    sum=sum+r**order
    n=n//10
    if(sum==k):
       print(f"{k} is armstrong number")
    else:
       print(f"{k} is not an armstrong number")
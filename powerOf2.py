n=int(input())
flag=0
while (n != 1):
    if (n % 2 != 0):
       flag=1
    n=n//2
if(flag==0):
    print("yes")
else:
    print("no")

n=int(input())
sum=0
l=[]
for i in range(n):
    if(i==0):
        l.append(0)
    elif(i==1):
        l.append(1)
    else:
        sum=sum+l[i-1]
        l.append(sum)
        sum=l[i-1]
if(n in l):
    print("it is fibonacci number")
else:
    print("it us not a fibonacci number")

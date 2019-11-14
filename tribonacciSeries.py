n=int(input())
sum=0
l=[]
for i in range(n):
    if(i==0):
        l.append(0)
    elif(i==1):
        l.append(1)
    else:
        sum=sum+l[i-1]+l[i-2]
        l.append(sum)
        sum=l[i-2]
print(l)

n=int(input())
res=[]
a=1
for i in range(n):
    res.append([])
    if(i==0):
        res[i].append(a)
        a+=1
    else:
        for j in range(0,i+1):
            res[i].append(a)
            a+=1
for i in range(n):
    print(*res[i])

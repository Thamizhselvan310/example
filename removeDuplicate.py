n=list(map(int,input().split()))
l=[]
for i in range(len(n)):
    if n[i] not in l:
        l.append(n[i])
print(*l)

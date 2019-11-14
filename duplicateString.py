s=input()
n={}
for i in range(0,len(s)):
    if s[i] not in n:
        n[s[i]] = 1
    else:
        n[s[i]] = n[s[i]] + 1
result = []
print(n)
for i in n:
    if n[i]!=1:
        result.append(i)
print(*result)

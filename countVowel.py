s=input()
volcount=0
constant=0
vol=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(s)):
    if(s[i] in vol):
        volcount+=1
    else:
        constant+=1
print("Vowels in string",volcount)
print("Constant in String",constant)

s=input()
v=c=d=sp=0
for i in s:
    if i.lower() in "aeiou":
        v+=1
    elif i.isdigit():
        d+=1
    elif i==" ":
        sp+=1
    else:
        c+=1
print(v,c,d,sp)

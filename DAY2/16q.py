text=input()
key=int(input())
res=""
for c in text:
    if c.isalpha():
        o=65 if c.isupper() else 97
        res+=chr((ord(c)-o+key)%26+o)
    else:
        res+=c
print(res)

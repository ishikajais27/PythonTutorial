t=float(input("Enter temperature: "))
u=input("Unit (C/F): ")
if u.upper()=="C":
    print((t*9/5)+32)
else:
    print((t-32)*5/9)

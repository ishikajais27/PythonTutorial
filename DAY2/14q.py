import re

s=input()
p=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
print("Valid" if re.match(p,s) else "Invalid")

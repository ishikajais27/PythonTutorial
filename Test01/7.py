n = int(input("Enter a number: "))
s = 0
temp = n
l = len(str(n))

while temp > 0:
    r = temp % 10
    s += r ** l
    temp //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

print("Triangle and Inverted Triangle Pattern")
n=int(input("Enter size: "))
print("Triangle:")
for i in range(1,n+1):
    print("*"*i)
print("Inverted Triangle:")
for i in range(n,0,-1):
    print("*"*i)

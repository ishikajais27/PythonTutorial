n=int(input())
if n<=1:
    print("Neither")
else:
    f=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            f=1
            break
    print("Prime" if f==0 else "Composite")

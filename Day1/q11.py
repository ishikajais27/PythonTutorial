
print("Pattern 1: Increasing triangle")
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

print("\nPattern 2: Repeated numbers")
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

print("\nPattern 3: Reverse triangle")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()
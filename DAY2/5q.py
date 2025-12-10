

a, b, c = map(int, input("Enter three numbers separated by space: ").split())

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

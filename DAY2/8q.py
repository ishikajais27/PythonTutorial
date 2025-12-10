a, b = map(int, input("Enter two numbers (start end): ").split())

print(f"Armstrong numbers between {a} and {b} are:")

for n in range(a, b + 1):
    s = str(n)
    length = len(s)
    if sum(int(d) ** length for d in s) == n:
        print(n)

d = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

print("Key with maximum value:", max(d, key=d.get))

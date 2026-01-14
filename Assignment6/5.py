# Q5: Tuple of even numbers

n = int(input("Enter number of elements: "))
tup = []

for i in range(n):
    tup.append(int(input("Enter element: ")))

tup = tuple(tup)
even_tuple = ()

for num in tup:
    if num % 2 == 0:
        even_tuple = even_tuple + (num,)

print("Original tuple:", tup)
print("Even numbers tuple:", even_tuple)

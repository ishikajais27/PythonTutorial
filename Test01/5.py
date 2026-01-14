t = tuple(map(int, input("Enter tuple elements: ").split()))
even = tuple(i for i in t if i % 2 == 0)
print("Even tuple:", even)

import numpy as np

n = int(input("Enter number of elements: "))
lst = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
arr = np.array(lst)
print("Array:", arr)
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)
print("Square of Array:", arr ** 2)

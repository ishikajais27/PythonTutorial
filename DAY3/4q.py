lst = [1, 2, 2, 3, 4, 3, 5]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print("Original list:", lst)
print("List without duplicates:", unique)

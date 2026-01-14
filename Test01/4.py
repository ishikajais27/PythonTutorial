lst = list(map(int, input("Enter list elements: ").split()))
new = []

for i in lst:
    if i not in new:
        new.append(i)

print("List after removing duplicates:", new)

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

common = []
for i in list1:
    for j in list2:
        if i == j and i not in common:
            common += [i]

print("Common elements:", common)

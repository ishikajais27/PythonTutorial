list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged_list = []
for i in list1:
    merged_list += [i]
for j in list2:
    merged_list += [j]

print("Merged list:", merged_list)

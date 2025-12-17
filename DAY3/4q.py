lst = list(map(int, input("Enter list elements: ").split()))
unique_list = []
for i in lst:
    if i not in unique_list:
        unique_list.append(i)
print("List without duplicates:", unique_list)

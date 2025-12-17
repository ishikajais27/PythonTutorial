dict1 = {}
dict2 = {}
n1 = int(input("Enter number of items for first dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("Enter number of items for second dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

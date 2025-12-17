d = {}
n = int(input("Enter number of items in dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

tuple_list = list(d.items())
print("Dictionary to list of tuples:", tuple_list)

new_dict = dict(tuple_list)
print("List of tuples back to dictionary:", new_dict)

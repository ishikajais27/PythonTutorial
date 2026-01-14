# Q6: Sort dictionary by values

n = int(input("Enter number of items: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))

print("Dictionary sorted by values:")
print(sorted_dict)

d = {}
n = int(input("Enter number of items in dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

sorted_by_key = dict(sorted(d.items()))
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))

print("Sorted by keys:", sorted_by_key)
print("Sorted by values:", sorted_by_value)

lst = [1, 2, 3, 2, 4, 2, 5]
element = 2
count = 0
for i in lst:
    if i == element:
        count += 1
print("List:", lst)
print("Occurrences of", element, ":", count)

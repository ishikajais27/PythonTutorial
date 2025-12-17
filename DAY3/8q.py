lst = [1, 2, 3, 4, 5]
k = 2
print("Original list:", lst)
print("Left rotation:", lst[k:] + lst[:k])
print("Right rotation:", lst[-k:] + lst[:-k])

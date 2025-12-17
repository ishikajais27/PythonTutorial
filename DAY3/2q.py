lst = list(map(int, input("Enter list elements: ").split()))
element = int(input("Enter element to count: "))

count = 0
for i in lst:
    if i == element:
        count += 1

print("Occurrences:", count)

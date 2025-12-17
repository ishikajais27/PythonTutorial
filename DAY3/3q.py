lst = list(map(int, input("Enter list elements: ").split()))
reversed_list = []
for i in lst:
    reversed_list = [i] + reversed_list
print("Reversed list:", reversed_list)

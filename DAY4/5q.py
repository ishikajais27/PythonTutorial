user_input = input("Enter elements of the list separated by spaces: ")
user_list = user_input.split()
unique_list = list(set(user_list))
print("List after removing duplicates:", unique_list)

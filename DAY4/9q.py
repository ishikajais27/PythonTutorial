directory = {}

while True:
    print("1. Add\n2. Search\n3. Update\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        directory[name] = number
        print("Added successfully")

    elif choice == "2":
        name = input("Enter name to search: ")
        print("Number:", directory.get(name, "Not found"))

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in directory:
            number = input("Enter new phone number: ")
            directory[name] = number
            print("Updated successfully")
        else:
            print("Name not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in directory:
            del directory[name]
            print("Deleted successfully")
        else:
            print("Name not found")

    elif choice == "5":
        break

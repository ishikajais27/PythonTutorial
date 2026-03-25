
phone_dir = {}

while True:
    print("\n--- PHONE DIRECTORY ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT
    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_dir[name] = number
        print("Contact added successfully!")

    # SEARCH CONTACT
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phone_dir:
            print(f"{name}'s number is {phone_dir[name]}")
        else:
            print("Contact not found!")

    # UPDATE CONTACT
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in phone_dir:
            new_number = input("Enter new number: ")
            phone_dir[name] = new_number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # DELETE CONTACT
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in phone_dir:
            del phone_dir[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # SHOW ALL CONTACTS
    elif choice == '5':
        if phone_dir:
            print("\nAll Contacts:")
            for name, number in phone_dir.items():
                print(f"{name}: {number}")
        else:
            print("No contacts available!")

    # EXIT
    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
# Contact Book Using Lists and Dictionaries

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contacts.append({
            "name": name,
            "phone": phone
        })

        print("Contact added!")

    elif ch == "2":
        name = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["name"] == name:
                print(c)
                found = True
                break

        if not found:
            print("Contact not found!")

    elif ch == "3":
        name = input("Enter name to update: ")

        for c in contacts:
            if c["name"] == name:
                c["phone"] = input("Enter new phone: ")
                print("Contact updated!")
                break
        else:
            print("Contact not found!")

    elif ch == "4":
        name = input("Enter name to delete: ")

        for c in contacts:
            if c["name"] == name:
                contacts.remove(c)
                print("Contact deleted!")
                break
        else:
            print("Contact not found!")

    elif ch == "5":
        for c in contacts:
            print("Name:", c["name"], "Phone:", c["phone"])

    elif ch == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

def add_student():
    with open("students.txt", "a") as f:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        f.write(roll + "," + name + "," + marks + "\n")

    print("Student added successfully!")


def display_students():
    try:
        with open("students.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No student records found.")


def search_student():
    roll = input("Enter Roll Number to search: ")

    try:
        with open("students.txt", "r") as f:
            for line in f:
                if line.startswith(roll + ","):
                    print("Student Record:", line.strip())
                    return

        print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def update_student():
    roll = input("Enter Roll Number to update: ")

    try:
        with open("students.txt", "r") as f:
            records = f.readlines()

        found = False

        with open("students.txt", "w") as f:
            for line in records:
                if line.startswith(roll + ","):
                    name = input("Enter New Name: ")
                    marks = input("Enter New Marks: ")

                    f.write(roll + "," + name + "," + marks + "\n")
                    found = True
                else:
                    f.write(line)

        print("Record updated!" if found else "Student not found.")

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n1.Add  2.Display  3.Search  4.Update  5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

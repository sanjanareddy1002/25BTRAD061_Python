# Attendance Tracker

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ").upper()

    students[name] = status

print("\n--- Attendance Report ---")

for name, status in students.items():
    print(name, ":", "Present" if status == "P" else "Absent")

    if status == "P":
        percentage = 100
    else:
        percentage = 0

    print("Attendance:", percentage, "%")

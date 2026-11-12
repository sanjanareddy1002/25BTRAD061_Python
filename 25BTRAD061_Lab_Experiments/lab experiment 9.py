# Student Grading System

students = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    students[name] = {
        "marks": marks,
        "grade": grade
    }

print("\n--- STUDENT RESULTS ---")

for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])
    print()

print("----------------------")

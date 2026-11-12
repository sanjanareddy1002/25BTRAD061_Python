import csv

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        print("Employee Payroll Summary")
        print("------------------------")

        for emp in reader:
            name = emp["Name"]
            basic = float(emp["Basic"])

            hra = basic * 0.20
            da = basic * 0.10

            gross = basic + hra + da
            deduction = gross * 0.05
            net = gross - deduction

            print("Name:", name)
            print("Gross Salary:", gross)
            print("Deductions:", deduction)
            print("Net Salary:", net)
            print("------------------------")

except FileNotFoundError:
    print("Employee CSV file not found.")

except (ValueError, KeyError):
    print("Invalid employee data in CSV file.")

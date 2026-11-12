# Log File Reader Program

# Creating a sample log file
with open("sample.log", "w") as file:
    file.write("INFO: Application started\n")
    file.write("ERROR: File not found\n")
    file.write("WARNING: Low memory\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database connection failed\n")
    file.write("INFO: Application running\n")
    file.write("WARNING: High CPU usage\n")

# Initializing counters
error_count = 0
warning_count = 0
info_count = 0

try:
    # Reading the log file
    with open("sample.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("----- LOG FILE SUMMARY -----")
    print("ERROR:", error_count)
    print("WARNING:", warning_count)
    print("INFO:", info_count)

except FileNotFoundError:
    print("Error: Log file not found.")

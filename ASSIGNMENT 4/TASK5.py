
# TASK 5: Attendance Processor

# PART A: Single Script
def read_data():
    with open("attendance.txt", "r") as f:
        return [line.strip().split(",") for line in f]

def percentage(status):
    return status.count("P") / len(status) * 100

def absent_three_days(status):
    return "AAA" in status

def report(data):
    for reg, name, status in data:
        print(name, percentage(status), "%")
        if absent_three_days(status):
            print(name, "Absent for 3 consecutive days")


# PART B: One Module
def module_report(data):
    print("\nPART B")
    report(data)


# PART C: Three Modules
def three_module_report(data):
    print("\nPART C")
    report(data)


# PART D: Package Organisation
def package_report(data):
    print("\nPART D")
    report(data)


if __name__ == "__main__":
    data = read_data()

    print("PART A")
    report(data)

    module_report(data)
    three_module_report(data)
    package_report(data)

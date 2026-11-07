attendance = {}

with open("attendance.txt", "r") as f:
    for line in f:
        try:
            reg, date, status = line.strip().split(",")
            if status not in ["P", "A"]:
                continue

            attendance[reg] = attendance.get(reg, [0, 0])
            attendance[reg][0] += 1
            if status == "P":
                attendance[reg][1] += 1
        except ValueError:
            print("Damaged line:", line.strip())

for reg, data in attendance.items():
    percentage = data[1] / data[0] * 100
    print(reg, percentage)


import os
import csv

def read_data(filename, errors):
    records = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                p = line.strip().split(",")

                if len(p) != 5 or not all(p):
                    errors.append([filename, line_no, "Damaged line"])
                else:
                    records.append((p, filename, line_no))

    except (FileNotFoundError, PermissionError,
            UnicodeDecodeError, OSError) as e:
        errors.append([filename, 0, str(e)])

    return records


def valid_email(email):
    p = email.split("@")
    return (len(p) == 2 and p[0] != ""
            and "." in p[1]
            and not any(c.isspace() for c in email))


def process(records, errors):
    valid = []
    seen = set()

    for p, filename, line_no in records:
        reg, name, dept, email, events = p

        if reg in seen:
            errors.append([filename, line_no, "Duplicate"])
        elif not valid_email(email):
            errors.append([filename, line_no, "Invalid email"])
        else:
            seen.add(reg)
            valid.append(p)

    return valid


def write_reports(records, errors):
    os.makedirs("output", exist_ok=True)

    with open("output/master_list.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Register", "Name", "Department", "Email", "Events"])
        w.writerows(records)

    event_data = {}

    for p in records:
        for event in p[4].split(";"):
            event_data.setdefault(event.strip(), []).append(p)

    for event, students in event_data.items():
        with open("output/" + event.replace(" ", "_") + ".csv",
                  "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Register", "Name", "Department", "Email"])
            for p in students:
                w.writerow(p[:4])

    with open("output/summary.txt", "w") as f:
        f.write("Total registrations: " + str(len(records)))
        f.write("\nTotal events: " + str(len(event_data)))

    with open("output/error_log.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["File", "Line", "Error"])
        w.writerows(errors)


if __name__ == "__main__":
    records = []
    errors = []

    for i in range(1, 6):
        filename = f"dept{i}.txt"
        records.extend(read_data(filename, errors))

    valid = process(records, errors)
    write_reports(valid, errors)

    print("Registration completed!")
    print("Valid registrations:", len(valid))
    print("Errors:", len(errors))

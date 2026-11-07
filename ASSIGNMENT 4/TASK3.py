class InvalidRecord(Exception):
    pass

def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord("Invalid fields")

    if parts[2] not in ["P", "A"]:
        raise InvalidRecord("Invalid status")

    return parts

def summarise(file):
    present = 0
    absent = 0
    errors = []

    try:
        with open(file, "r") as f:
            for i, line in enumerate(f, 1):
                try:
                    data = parse_line(line)
                    if data[2] == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as e:
                    errors.append((i, str(e)))

    except FileNotFoundError:
        print("File not found")

    return present, absent, errors

print(summarise("attendance.txt"))

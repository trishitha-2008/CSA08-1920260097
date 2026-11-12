class InvalidRecord(Exception):
    pass

def parse_line(line):
    p = line.strip().split(",")
    if len(p) != 3:
        raise InvalidRecord("Invalid fields")
    if p[2] not in ("P", "A"):
        raise InvalidRecord("Invalid status")
    return p

def summarise(path):
    present = absent = 0
    errors = []

    try:
        with open(path) as f:
            for n, line in enumerate(f, 1):
                try:
                    p = parse_line(line)
                    if p[2] == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as e:
                    errors.append((n, str(e)))
    except FileNotFoundError:
        errors.append((0, "File not found"))

    return present, absent, errors

print(summarise("attendance.csv"))

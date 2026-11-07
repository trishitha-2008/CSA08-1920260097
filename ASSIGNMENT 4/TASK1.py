def calculate(file):
    total = 0
    rejected = []

    with open(file, "r") as f:
        for line in f:
            try:
                parts = line.strip().split(",")
                total += float(parts[2])
                print(parts[1], parts[2])
            except (ValueError, IndexError):
                rejected.append(line.strip())

    print("Total:", total)
    print("Rejected:", rejected)

calculate("mess.txt")

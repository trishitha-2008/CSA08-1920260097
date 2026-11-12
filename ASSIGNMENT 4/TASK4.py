def save_returns(books):
    with open("returns.log", "a") as f:
        for book in books:
            f.write(book + "\n")

def process(filename):
    try:
        with open(filename) as f:
            save_returns(f.read().splitlines())
    except FileNotFoundError as e:
        with open("error.log", "a") as f:
            f.write(str(e) + "\n")

for name in ["day1.txt", "day2.txt", "day3.txt"]:
    process(name)

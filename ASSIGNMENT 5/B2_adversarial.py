
import csv
import io
import sqlite3

def test_file(data):
    try:
        reader = csv.DictReader(io.StringIO(data))

        if not reader.fieldnames or not {"station", "date", "pm25"}.issubset(reader.fieldnames):
            print("Error: Missing column")
            return

        for row in reader:
            print(row)

    except Exception as e:
        print("Error:", e)


# Missing column
print("Missing Column:")
test_file("station,date\nAdyar,2026-10-01")

# Wrong delimiter
print("\nWrong Delimiter:")
test_file("station;date;pm25\nAdyar;2026-10-01;48")

# Different encoding simulation
print("\nEncoding:")
try:
    data = b"station,date,pm25\nAdyar,2026-10-01,48"
    print(data.decode("ascii"))
except UnicodeDecodeError:
    print("Encoding error")

# Empty file
print("\nEmpty File:")
test_file("")

# SQL injection comparison
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE aq (station TEXT)")
con.execute("INSERT INTO aq VALUES ('Adyar')")

name = "Adyar' OR '1'='1"

# Unsafe query
query = "SELECT * FROM aq WHERE station = '" + name + "'"
print("\nUnsafe:", con.execute(query).fetchall())

# Safe query
print("Safe:", con.execute(
    "SELECT * FROM aq WHERE station = ?", (name,)
).fetchall())

con.close()

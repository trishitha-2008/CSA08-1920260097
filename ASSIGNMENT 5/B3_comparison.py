
import csv
import io
import sqlite3
import pandas as pd
import random
import time
import cProfile
from collections import defaultdict
from datetime import date, timedelta

random.seed(10)

# Generate data
def generate_data(stations):
    rows = []
    start = date(2026, 1, 1)

    for s in range(stations):
        for d in range(365):
            day = start + timedelta(days=d)

            for hour in range(24):
                rows.append((
                    f"Station{s+1}",
                    str(day),
                    round(random.uniform(10, 150), 2)
                ))

    return rows


# Method 1: Python loops
def python_method(rows):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for station, day, pm in rows:
        key = (station, day)
        totals[key] += pm
        counts[key] += 1

    return {key: totals[key] / counts[key] for key in totals}


# Method 2: Pandas
def pandas_method(rows):
    df = pd.DataFrame(rows, columns=["station", "day", "pm25"])
    return df.groupby(["station", "day"])["pm25"].mean()


# Method 3: SQL
def sql_method(rows):
    con = sqlite3.connect(":memory:")

    con.execute("""
        CREATE TABLE readings (
            station TEXT,
            day TEXT,
            pm25 REAL
        )
    """)

    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)", rows
    )

    result = con.execute("""
        SELECT station, day, AVG(pm25)
        FROM readings
        GROUP BY station, day
    """).fetchall()

    con.close()
    return result


# Small data correctness check
small = [
    ("Adyar", "2026-10-01", 40),
    ("Adyar", "2026-10-01", 60),
    ("Guindy", "2026-10-01", 90)
]

a = python_method(small)
b = pandas_method(small).to_dict()
c = sql_method(small)

print("Python:", a)
print("Pandas:", b)
print("SQL:", c)

# Compare timings
for n in [1, 12, 120]:
    data = generate_data(n)

    for name, func in [
        ("Python", python_method),
        ("Pandas", pandas_method),
        ("SQL", sql_method)
    ]:
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()

        print(n, name, round(end - start, 4), "seconds")


# Profile Python method
data = generate_data(1)
cProfile.run("python_method(data)")

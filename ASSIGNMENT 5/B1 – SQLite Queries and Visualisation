
import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict

con = sqlite3.connect("air_quality.db")

con.execute("""
CREATE TABLE IF NOT EXISTS readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    clean
)

con.commit()

# Query 1: Average PM2.5 in October
print(con.execute("""
SELECT station, AVG(pm25)
FROM readings
WHERE day LIKE '2026-10-%'
GROUP BY station
""").fetchall())

# Query 2: Highest reading
print(con.execute("""
SELECT station, MAX(pm25)
FROM readings
GROUP BY station
""").fetchall())

# Query 3: Daily average
print(con.execute("""
SELECT station, day, AVG(pm25)
FROM readings
GROUP BY station, day
""").fetchall())

# Line chart
for station in set(row[0] for row in clean):
    data = [r for r in clean if r[0] == station]
    plt.plot(
        [r[1] for r in data],
        [r[2] for r in data],
        marker="o",
        label=station
    )

plt.title("PM2.5 Monthly Trend")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("trend.png")
plt.show()

con.close()

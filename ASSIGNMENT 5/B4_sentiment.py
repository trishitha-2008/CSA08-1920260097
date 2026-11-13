
import re
import sqlite3
import time

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}


# TODO 1: Sentiment scorer
def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0

    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0

        if i > 0 and words[i - 1] in NEGATORS:
            value = -value

        total += value

    return total


def label(text):
    s = score(text)

    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    return "neutral"


# Extractive summariser
def summarise(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    words = re.findall(r'\b[a-z]+\b', text.lower())

    stopwords = {"the", "is", "and", "was", "are", "from", "a", "to"}

    frequency = {}

    for word in words:
        if word not in stopwords:
            frequency[word] = frequency.get(word, 0) + 1

    if not sentences:
        return ""

    return max(
        sentences,
        key=lambda sentence: sum(
            frequency.get(word, 0)
            for word in re.findall(r'\b[a-z]+\b', sentence.lower())
        )
    )


# 50 complaints
complaints = [
    "Roads are clean and buses are fast.",
    "Smoke from factory makes the air bad.",
    "The staff were not helpful.",
    "Not bad, service improved.",
    "The road is dirty and broken.",
    "Air quality is good today.",
    "Traffic is slow and smoke is high.",
    "The workers are helpful.",
    "The pollution is bad.",
    "The water is clean.",
] * 5

print("Sentiment Results")

for complaint in complaints:
    print(label(complaint), "|", summarise(complaint))

# Compare with manual labels
manual = [
    "positive", "negative", "negative", "positive",
    "negative", "positive", "negative", "positive",
    "negative", "positive"
] * 5

correct = 0

for complaint, expected in zip(complaints, manual):
    if label(complaint) == expected:
        correct += 1

print("Agreement:", correct, "/ 50")
print("Accuracy:", correct / 50 * 100, "%")


# Database index test
con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

data = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0)
] * 10000

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)", data
)

def measure():
    start = time.perf_counter()

    for _ in range(100):
        con.execute(
            "SELECT AVG(pm25) FROM readings WHERE station=? AND day=?",
            ("Adyar", "2026-10-01")
        ).fetchone()

    return time.perf_counter() - start


before = measure()
con.execute("CREATE INDEX idx_station_day ON readings(station, day)")
after = measure()

print("Before Index:", before)
print("After Index:", after)

con.close()

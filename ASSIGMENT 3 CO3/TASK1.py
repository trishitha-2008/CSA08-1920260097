import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
max_rain = max(readings)
min_rain = min(readings)

max_day = readings.index(max_rain) + 1
min_day = readings.index(min_rain) + 1

# Naive moving average
def naive_average(data):
    return [
        sum(data[i:i+7]) / 7
        for i in range(len(data) - 6)
    ]

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total += data[i] - data[i-7]
        result.append(total / 7)

    return result

averages = running_average(readings)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Weekly totals:", weekly_totals)
print("Maximum rainfall:", max_rain, "on day", max_day)
print("Minimum rainfall:", min_rain, "on day", min_day)
print("7-day moving averages:", averages[:10])
print("Dry days:", dry_days)

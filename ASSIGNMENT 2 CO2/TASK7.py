# Q7 - Diagnose, Redesign and Validate
# Selected program: Building long text using += and join()

import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


# Original method
def original_program(parts):
    text = ""

    for item in parts:
        text += item + ";"

    return text


# Redesigned method
def redesigned_program(parts):
    return "".join(item + ";" for item in parts)


# Compare both methods
for size in [1000, 10000, 200000]:
    data = items[:size]

    start = time.perf_counter()
    original_result = original_program(data)
    original_time = time.perf_counter() - start

    start = time.perf_counter()
    redesigned_result = redesigned_program(data)
    redesigned_time = time.perf_counter() - start

    print("\nNumber of items:", size)
    print("Original length:", len(original_result))
    print("Redesigned length:", len(redesigned_result))
    print("Same output:", original_result == redesigned_result)
    print("Original time:", round(original_time, 4), "seconds")
    print("Redesigned time:", round(redesigned_time, 4), "seconds")

    if redesigned_time > 0:
        improvement = original_time / redesigned_time
        print("Speed ratio:", round(improvement, 2))

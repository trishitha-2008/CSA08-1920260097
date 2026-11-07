households = [
    (100, False, False),
    (101, True, False),
    (150, True, False),
    (200, False, False),
    (201, False, True),
    (250, False, False),
    (80, False, False),
    (180, False, True)
]

def subsidy_separate(units, ration, senior):
    results = []

    if units <= 100:
        results.append("Full subsidy")

    if 101 <= units <= 200 and ration:
        results.append("Partial subsidy")

    if units > 200 and senior:
        results.append("Special subsidy")

    if not results:
        results.append("No subsidy")

    return results


def subsidy_elif(units, ration, senior):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and ration:
        return "Partial subsidy"
    elif units > 200 and senior:
        return "Special subsidy"
    else:
        return "No subsidy"


for units, ration, senior in households:
    print("Units:", units)
    print("Separate if:", subsidy_separate(units, ration, senior))
    print("If-elif-else:", subsidy_elif(units, ration, senior))
    print()

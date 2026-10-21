def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40
    rate += snf_steps * 0.30

    return round(rate, 2)


def payout(litres, fat, snf):
    return round(
        litres * rate_per_litre(fat, snf), 2
    )


def ten_day_total(entries):
    total = 0

    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)

    return round(total, 2)


entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

for entry in entries:
    print("Payment:", payout(*entry))

print("Ten-day total:", ten_day_total(entries))

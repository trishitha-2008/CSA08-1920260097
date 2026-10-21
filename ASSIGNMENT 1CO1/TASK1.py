BASE_RATE = 30.00

entries = [
    ("F001", 10, 3.5, 8.5),
    ("F002", 8.5, 4.2, 8.7)
]

total = 0

for farmer, litres, fat, snf in entries:
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * 0.40
    rate += snf_steps * 0.30

    payment = round(litres * rate, 2)
    total += payment

    print(farmer, "Rate:", round(rate, 2))
    print("Payment:", payment)

print("Total:", round(total, 2))

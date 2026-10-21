litres = float(input("Enter litres: "))
fat = float(input("Enter fat: "))
snf = float(input("Enter SNF: "))

if litres < 0:
    print("Invalid litres")
elif fat < 2 or fat > 7:
    print("Invalid fat")
elif snf < 0:
    print("Invalid SNF")
else:
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40
    rate += snf_steps * 0.30

    payment = round(litres * rate, 2)

    print(f"Rate: Rs. {rate:.2f}")
    print(f"Payment: Rs. {payment:.2f}")

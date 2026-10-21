BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

value = 10
print(value, type(value))

value = "Milk"
print(value, type(value))

a = 10
b = 20

a, b = b, a

print("A =", a)
print("B =", b)

rate_card = {
    "base_rate": BASE_RATE,
    "fat_value": FAT_STEP_VALUE,
    "snf_value": SNF_STEP_VALUE
}

print(rate_card)

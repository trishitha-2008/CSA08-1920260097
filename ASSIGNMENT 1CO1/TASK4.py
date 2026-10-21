import math

fat = 4.2
snf = 8.7
litres = 8.5

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30 + fat_steps * 0.40
rate += snf_steps * 0.30

payment = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", round(rate, 2))
print("Payment:", payment)

print("Floor:", math.floor(-7 / 2))
print("Integer:", int(-7 / 2))
print("Float:", 0.1 + 0.2)

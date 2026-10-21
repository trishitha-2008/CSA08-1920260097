from decimal import Decimal

print(type(10))
print(type(10.5))
print(type("Hello"))
print(type(True))
print(type([10, 20]))

print(7 / 2)
print(7 // 2)
print(7 % 2)
print(-7 // 2)

print(0.1 + 0.2 == 0.3)

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)
print(a + b == Decimal("0.3"))

payments = ["10.10", "20.20", "30.30"]

total = Decimal("0.00")

for payment in payments:
    total += Decimal(payment)

print("Total:", total)

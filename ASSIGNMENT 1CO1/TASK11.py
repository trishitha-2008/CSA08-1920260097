from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_VALUE = Decimal("0.40")
SNF_VALUE = Decimal("0.30")


def rate_per_litre(fat, snf):
    fat = Decimal(fat)
    snf = Decimal(snf)

    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat")

    if snf < 0:
        raise ValueError("Invalid SNF")

    fat_steps = ((fat - Decimal("3.5")) /
                 Decimal("0.1")).quantize(Decimal("1"))

    snf_steps = ((snf - Decimal("8.5")) /
                 Decimal("0.1")).quantize(Decimal("1"))

    rate = BASE_RATE + fat_steps * FAT_VALUE
    rate += snf_steps * SNF_VALUE

    return rate.quantize(Decimal("0.01"))


def payout(litres, fat, snf):
    litres = Decimal(litres)

    if litres < 0:
        raise ValueError("Invalid litres")

    payment = litres * rate_per_litre(fat, snf)
    return payment.quantize(Decimal("0.01"))


print("Payment:", payout("8.5", "4.2", "8.7"))

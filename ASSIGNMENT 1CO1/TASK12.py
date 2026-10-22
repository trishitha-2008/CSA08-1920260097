from decimal import Decimal, ROUND_HALF_UP

STEP = Decimal("0.10")
STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")

RATE_CARDS = {
    "regular": {
        "base": Decimal("30.00"),
        "fat": Decimal("0.40")
    },
    "april_june": {
        "base": Decimal("32.00"),
        "fat": Decimal("0.45")
    }
}

SNF_VALUE = Decimal("0.30")
BONUS_LIMIT = Decimal("500")
BONUS_RATE = Decimal("0.50")


def round_steps(value):
    return (value / STEP).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP
    )


def rate_per_litre(fat, snf, season="regular"):
    fat = Decimal(fat)
    snf = Decimal(snf)

    if season not in RATE_CARDS:
        raise ValueError("Invalid season")

    if not Decimal("2.00") <= fat <= Decimal("7.00"):
        raise ValueError("Invalid fat")

    if snf < 0:
        raise ValueError("Invalid SNF")

    card = RATE_CARDS[season]

    fat_steps = round_steps(fat - STANDARD_FAT)
    snf_steps = round_steps(snf - STANDARD_SNF)

    rate = card["base"] + fat_steps * card["fat"]
    rate += snf_steps * SNF_VALUE

    return rate.quantize(Decimal("0.01"))


def payout(litres, fat, snf, season="regular"):
    litres = Decimal(litres)

    if litres < 0:
        raise ValueError("Invalid litres")

    rate = rate_per_litre(fat, snf, season)

    return (litres * rate).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def ten_day_payment(entries, season="regular"):
    total_litres = sum(
        (Decimal(e[0]) for e in entries),
        Decimal("0")
    )

    base_total = sum(
        (payout(*e, season) for e in entries),
        Decimal("0.00")
    )

    bonus = Decimal("0.00")

    if total_litres > BONUS_LIMIT:
        bonus = (total_litres * BONUS_RATE).quantize(
            Decimal("0.01")
        )

    final_total = base_total + bonus

    return base_total, bonus, final_total


entries = [
    ("250.00", "4.25", "8.65"),
    ("260.50", "3.55", "8.50")
]

base, bonus, final = ten_day_payment(
    entries, "april_june"
)

print("Base payment:", base)
print("Bonus:", bonus)
print("Final payment:", final)

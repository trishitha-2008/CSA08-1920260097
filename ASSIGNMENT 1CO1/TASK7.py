BASE_RATE = 30.00


def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * 0.40
    rate += snf_steps * 0.30

    return round(rate, 2)


def payout(litres, fat, snf):
    return round(
        litres * rate_per_litre(fat, snf), 2
    )


if __name__ == "__main__":
    print(rate_per_litre(4.2, 8.7))

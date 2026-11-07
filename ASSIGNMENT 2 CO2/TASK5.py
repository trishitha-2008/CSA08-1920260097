def customer(name, items=None):
    if items is None:
        items = []

    items.append(name)
    return items

print(customer("Ravi"))
print(customer("Priya"))

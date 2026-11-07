contacts = [
    {"name": "Ravi", "phone": "98765", "email": "ravi@gmail.com"},
    {"name": "Ravi", "phone": "98765", "email": "ravi2@gmail.com"},
    {"name": "Priya", "phone": "98766", "email": "priya@gmail.com"}
]

merged = {}

for c in contacts:
    phone = c["phone"]

    if phone not in merged:
        merged[phone] = {
            "name": c["name"],
            "emails": set()
        }

    merged[phone]["emails"].add(c["email"])

print("Merged contacts:")
print(merged)

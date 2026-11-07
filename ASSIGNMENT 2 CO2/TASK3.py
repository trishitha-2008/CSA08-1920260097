number = input("Enter vehicle number: ").upper().strip()

if len(number) >= 6 and number[:2].isalpha() and number[-4:].isdigit():
    print("Valid:", number)
else:
    print("Invalid vehicle number")

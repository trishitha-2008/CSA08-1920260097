income = int(input("Enter annual income: "))

if income <= 100:
    print("Full subsidy")
elif income <= 200:
    print("Half subsidy")
else:
    print("No subsidy")

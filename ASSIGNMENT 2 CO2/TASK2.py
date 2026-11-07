correct_otp = "1234"

# While loop
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp.strip() == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP verified successfully")
        break
    else:
        print("Wrong OTP")

    if attempts == 2:
        pass

else:
    print("Account locked for 30 minutes")


# For loop
for attempt in range(3):
    otp = input("Enter OTP: ")

    if otp.strip() == "":
        print("Blank entry. Try again.")
        continue

    if otp == correct_otp:
        print("OTP verified successfully")
        break

    print("Wrong OTP")

else:
    print("Account locked for 30 minutes")


# Recursive OTP verification
def verify_otp(attempts=0):
    if attempts == 3:
        print("Account locked for 30 minutes")
        return

    otp = input("Enter OTP: ")

    if otp.strip() == "":
        print("Blank entry. Try again.")
        verify_otp(attempts)
        return

    if otp == correct_otp:
        print("OTP verified successfully")
        return

    print("Wrong OTP")
    verify_otp(attempts + 1)


# Uncomment to test recursion
# verify_otp()

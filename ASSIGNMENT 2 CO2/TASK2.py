correct_otp = "1234"

for i in range(3):
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank OTP")
        continue

    if otp == correct_otp:
        print("Login successful")
        break
else:
    print("Maximum attempts reached")

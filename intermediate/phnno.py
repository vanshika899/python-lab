import re

number = input("Enter mobile number: ")

pattern = r"^[789]\d{9}$"

if re.match(pattern, number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

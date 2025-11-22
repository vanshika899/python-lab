import datetime

name = input("Enter your name: ")
dob = input("Enter your date of birth (dd-mm-yyyy): ")

try:
    datetime.datetime.strptime(dob, "%d-%m-%Y")
    print("Details recorded")
except:
    raise Exception("Invalid date entered")

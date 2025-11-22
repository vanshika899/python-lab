name = input("Enter your name: ")

if name == "Rahul":
    raise Exception("Access denied. Please quit the program.")
else:
    print("Hello", name)

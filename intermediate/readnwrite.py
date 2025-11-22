file = open("hello.txt", "w")
file.write("Hello, this is a file write operation.")
file.close()

file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()

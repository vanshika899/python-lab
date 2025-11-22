f = open("hello.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    print(line[::-1])

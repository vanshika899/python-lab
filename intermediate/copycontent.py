src = open("hello.txt", "r")
data = src.read()
src.close()

dest = open("hello2.txt", "w")
dest.write(data)
dest.close()

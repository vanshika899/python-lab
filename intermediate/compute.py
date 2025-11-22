f = open("hello.txt", "r")
text = f.read()
f.close()

chars = len(text)
words = len(text.split())
lines = len(text.split("\n"))

print("Characters:", chars)
print("Words:", words)
print("Lines:", lines)

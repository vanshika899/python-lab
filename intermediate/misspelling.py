import string

filename = input("Enter file name: ")

try:
    file = open(filename, "r")
except:
    print("Error: Cannot open file.")
    exit()

known_file = open("hello.txt", "r")
known_words = set(known_file.read().lower().split())
known_file.close()

text = file.read()
file.close()

for word in text.split():
    cleaned = word.strip(string.punctuation).lower()
    if cleaned and cleaned not in known_words:
        print("Misspelled:", cleaned)

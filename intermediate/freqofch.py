f = open("hello.txt", "r")
text = f.read()
f.close()

freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

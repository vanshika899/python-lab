a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print(x)

new_list = [x for x in a if x < 5]
print(new_list)

print([x for x in a if x < 5])

n = int(input("Enter a number: "))
result = [x for x in a if x < n]
print(result)

def find_number(lst, num):
    return num in lst

a = [1, 3, 5, 7, 9, 11]
n = int(input("Enter a number: "))
print(find_number(a, n))

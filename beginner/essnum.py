import random

num = random.randint(1, 9)
guess = int(input("Guess the number (1-9): "))

if guess < num:
    print("Too low")
elif guess > num:
    print("Too high")
else:
    print("Exactly right!")

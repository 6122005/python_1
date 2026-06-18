# age = 20
# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# a = 10
# b = 20

# print(a < b)

# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# for i in range(5):
#     print(i)

# for i in range(1, 7):
#     print(i)

import random

# Computer generates random number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("🎉 Congratulations!")
        print("Correct Number:", secret_number)
        print("Attempts:", attempts)
        break
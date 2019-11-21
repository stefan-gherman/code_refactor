import math
import random

NUMBERS_IN_LIST = 10

numbers_up_to_99 = []

for number in range(NUMBERS_IN_LIST):
    numbers_up_to_99.append(random.randint(1, 99))

print(numbers_up_to_99)
for index in range(10):
    guess = int(input("Enter an integer from 1 to 99: "))
    while numbers_up_to_99[index] != guess:
        if guess < numbers_up_to_99[index]:
            print("guess is low")
        elif guess > numbers_up_to_99[index]:
            print("guess is high")
        else:
            break
        guess = int(input("Enter an integer from 1 to 99: "))
    print("you guessed it!")

numbers_up_to_49 = []
for number in range(NUMBERS_IN_LIST):
    numbers_up_to_49.append(random.randint(1, 49))

for index in range(10):
    guess = int(input("Enter an integer from 1 to 49: "))
    while numbers_up_to_49[index] != guess:
        if guess < numbers_up_to_49[index]:
            print("guess is low")
        elif guess > numbers_up_to_49[index]:
            print("guess is high")
        else:
            break
        guess = int(input("Enter an integer from 1 to 49: "))
    print("you guessed it!")

import math
import random

numbers_up_to_99 = []
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))
numbers_up_to_99.append(random.randint(1, 99))

for index in range(10):
    guess = int(input("Enter an integer from 1 to 99: "))
    while numbers_up_to_99[index] != guess:
        if guess < numbers_up_to_99[index]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > numbers_up_to_99[index]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

numbers_up_to_49 = []
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))
numbers_up_to_49.append(random.randint(1, 49))

for index in range(10):
    guess = int(input("Enter an integer from 1 to 49: "))
    while numbers_up_to_49[index] != guess:
        if guess < numbers_up_to_49[index]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 49: "))
        elif guess > numbers_up_to_49[index]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")

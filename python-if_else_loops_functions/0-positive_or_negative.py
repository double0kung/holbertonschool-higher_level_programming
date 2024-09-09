#!/usr/bin/python3
# This program will assign a random signed number to the variable number
# each time it is executed and print whether the number stored in the
# variable number is positive or negative.
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

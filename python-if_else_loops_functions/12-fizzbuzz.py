#!/usr/bin/python3
# This program contains a function that prints the numbers from 1 to 100
# separated by a space, replacing multiples of 3 with "Fizz", multiples of 5
# with "Buzz", and multiples of both with "FizzBuzz".
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

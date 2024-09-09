#!/usr/bin/python3
# This program contains a function that prints a string in uppercase
# followed by a new line.
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) - 32 if ord('a') <= ord(c) <= ord('z')
                            else ord(c)), end="")
    print("")

#!/usr/bin/python3
# This program contains a function that prints a string in uppercase
# followed by a new line.
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}\n".format(result), end="")

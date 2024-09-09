#!/usr/bin/python3
# This program prints the ASCII alphabet in lowercase, not followed by a new
# line, excluding the letters 'q' and 'e'.
for char in range(97, 123):
    if char != 101 and char != 113:
        print("{:c}".format(char), end="")

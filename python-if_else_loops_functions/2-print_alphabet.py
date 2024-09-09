#!/usr/bin/python3
# This program prints the ASCII alphabet in lowercase, not followed by a new
# line.
for char in range(97, 123):
    print("{:c}".format(char), end="")
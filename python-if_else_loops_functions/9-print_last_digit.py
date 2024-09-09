#!/usr/bin/python3
# This program contains a function that prints the last digit of a number.

def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

# Test code to test the function directly:
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
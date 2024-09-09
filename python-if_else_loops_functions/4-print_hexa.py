#!/usr/bin/python3
# This program prints all numbers from 0 to 98 in decimal and in
# hexadecimal.
for num in range(99):
    print("{} = 0x{:x}".format(num, num))
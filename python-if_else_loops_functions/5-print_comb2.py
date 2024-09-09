#!/usr/bin/python3
# This program prints numbers from 0 to 99, separated by ', '.
for num in range(100):
    if num == 99:
        print("{:02d}".format(num))
    else:
        print("{:02d}".format(num), end=", ")

#!/usr/bin/python3
# This program prints numbers from 0 to 99, separated by ', '.
for i in range(100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")

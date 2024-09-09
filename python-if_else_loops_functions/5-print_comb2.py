#!/usr/bin/python3
# This program prints numbers from 0 to 99, separated by ', '.
for i in range(100):
    print("{:02d}".format(i), end="\n" if i == 99 else ", ")

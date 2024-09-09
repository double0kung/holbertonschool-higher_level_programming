#!/usr/bin/python3
# This program contains a function that checks for lowercase character.

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

# to test the function directly:
if __name__ == "__main__":
     print("a is {}".format("lower" if islower("a") else "upper"))
     print("H is {}".format("lower" if islower("H") else "upper"))
     print("A is {}".format("lower" if islower("A") else "upper"))
     print("3 is {}".format("lower" if islower("3") else "upper"))
     print("g is {}".format("lower" if islower("g") else "upper"))
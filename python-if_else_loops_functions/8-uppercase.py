#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) - 32 if ord('a') <= ord(c) <= ord('z') else ord(c)), end="")
    print("")

# Test code to test the function directly:
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
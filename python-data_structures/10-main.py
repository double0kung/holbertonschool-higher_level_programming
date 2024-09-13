#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Additional tests
print(max_integer([]))  # Empty list
print(max_integer([42]))  # Single element list
print(max_integer([-1, -5, -3, -2]))  # List with negative numbers
print(max_integer([100, 10, 10, 100]))  # List with repeated max value

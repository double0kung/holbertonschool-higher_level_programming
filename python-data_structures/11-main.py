#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

# Additional tests
print("\nAdditional tests:")
print(divisible_by_2([]))  # Empty list
print(divisible_by_2([1, 3, 5]))  # List with no even numbers
print(divisible_by_2([2, 4, 6]))  # List with all even numbers

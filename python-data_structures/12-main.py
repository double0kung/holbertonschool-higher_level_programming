#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

# Additional tests
print("\nAdditional tests:")
print(delete_at([1, 2, 3], 0))  # Delete first element
print(delete_at([1, 2, 3], 2))  # Delete last element
print(delete_at([1, 2, 3], 3))  # Index out of range
print(delete_at([1, 2, 3], -1))  # Negative index
print(delete_at([], 0))  # Empty list

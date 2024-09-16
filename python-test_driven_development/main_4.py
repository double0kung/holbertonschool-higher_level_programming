#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

try:
    print(matrix_divided([[3, "9"], [15, 3]], 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[3, 9], [15, 3]], "3"))
except Exception as e:
    print(e)

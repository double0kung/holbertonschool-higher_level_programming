#!/usr/bin/env python3
from task_01_duck_typing import Circle

def test_circle_negative():
    circle_negative = Circle(-5)
    assert abs(circle_negative.area() - 78.53981633974483) < 1e-5, "Area should handle negative radius"
    assert abs(circle_negative.perimeter() - 31.41592653589793) < 1e-5, "Perimeter should handle negative radius"
    print("All tests passed!")

if __name__ == "__main__":
    test_circle_negative()

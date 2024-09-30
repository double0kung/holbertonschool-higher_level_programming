#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

def test_circle_area():
    circle = Circle(5)
    assert abs(circle.area() - 78.53981633974483) < 1e-5, "Circle area calculation is incorrect"
    print("Circle area test passed!")

if __name__ == "__main__":
    test_circle_area()

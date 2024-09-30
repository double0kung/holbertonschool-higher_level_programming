#!/usr/bin/env python3
"""Module for Shape abstract class, Circle and Rectangle classes, and shape_info function"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass

class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle"""
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

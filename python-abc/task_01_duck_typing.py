#!/usr/bin/env python3
"""Module for Shape abstract class and Circle class"""

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

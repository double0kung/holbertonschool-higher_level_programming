#!/usr/bin/env python3
"""Module for Animal abstract class and its subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass

class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Implement the sound method for Dog"""
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Implement the sound method for Cat"""
        return "Meow"

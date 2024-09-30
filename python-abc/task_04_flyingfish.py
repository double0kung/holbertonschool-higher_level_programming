#!/usr/bin/env python3
"""Module for Fish, Bird, and FlyingFish classes"""

class Fish:
    """Fish class"""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """Bird class"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from Fish and Bird"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Demonstrating Method Resolution Order
print("Method Resolution Order:", FlyingFish.mro())

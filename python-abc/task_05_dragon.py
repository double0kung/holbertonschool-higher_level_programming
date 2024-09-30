#!/usr/bin/env python3
"""Module for SwimMixin, FlyMixin, and Dragon classes"""

class SwimMixin:
    """Mixin class for swimming ability"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class for flying ability"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")

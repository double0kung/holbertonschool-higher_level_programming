# Python - More Classes and Objects

This project is part of the Higher Level Programming curriculum at Holberton School. It focuses on advancing your understanding of Object-Oriented Programming (OOP) in Python, specifically working with classes and objects.

## Project Overview

In this project, we incrementally build a `Rectangle` class, adding more functionality with each task. The project covers various OOP concepts such as:

- Class and instance attributes
- Properties and methods
- Static and class methods
- Special methods (__str__, __repr__, __del__)

## Files and Descriptions

0. **0-rectangle.py**: Simple empty class Rectangle that defines a rectangle.
1. **1-rectangle.py**: Class Rectangle with private instance attributes width and height.
2. **2-rectangle.py**: Adds area and perimeter methods to the Rectangle class.
3. **3-rectangle.py**: Adds string representation to print the rectangle with '#'.
4. **4-rectangle.py**: Adds __repr__ method for string representation of the rectangle.
5. **5-rectangle.py**: Adds functionality to print a message when an instance is deleted.
6. **6-rectangle.py**: Adds a public class attribute to count the number of instances.
7. **7-rectangle.py**: Adds a public class attribute to customize the string representation.
8. **8-rectangle.py**: Adds a static method to compare rectangle areas.
9. **9-rectangle.py**: Adds a class method to create a square.

## How to Use

Each file can be executed independently. Here's an example of how to use the Rectangle class:

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
```

## Requirements

- All files interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
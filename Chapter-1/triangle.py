# Enter you module contents here
"""Contains functions that deal with calculating lengths and areas of a right-angle triangle
"""

__author__ = "Lukas Rhoades"
__version__ = "1.0"

def hypotenuse(a, b):
    """Returns length of hypotenuse when input length of two other sides of right triangle
    """
    from math import sqrt
    return sqrt(a**2 + b**2)

def area(a, b):
    """Returns area of right triangle when input two perpendicular sides
    """
    return 0.5 * (a * b)

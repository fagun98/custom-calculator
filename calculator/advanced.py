import math

class AdvancedCalculator:
    """Class for advanced mathematical operations."""

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(a)

    @staticmethod
    def power(a, b):
        return math.pow(a, b)

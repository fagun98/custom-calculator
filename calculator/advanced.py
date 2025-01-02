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

    @staticmethod
    def logarithm(a, base=10):
        if a <= 0:
            raise ValueError("Logarithm is undefined for non-positive numbers.")
        return math.log(a, base)
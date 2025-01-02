import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)

def power(a, b):
    return math.pow(a, b)

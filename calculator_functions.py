"""
Module with mathematical functions for the calculator
"""

def add(a, b):
    """Adds two numbers"""
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Calculates a raised to the power of b"""
    return a ** b


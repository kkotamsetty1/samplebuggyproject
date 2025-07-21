# calculator.py

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """
    Divides two numbers.
    Raises ValueError if the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    Raises ValueError for negative input.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

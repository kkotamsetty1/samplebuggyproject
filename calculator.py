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
    ISSUE 1: Does not handle division by zero.
    """
    return a / b

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    ISSUE 2: Does not correctly handle negative input.
    INEFFICIENCY 1: Simple iterative approach, could be less efficient for very large numbers
                   compared to more optimized or memoized solutions.
    """
    if n == 0:
        return 1
    # Bug: For negative numbers, this loop won't execute or will cause issues.
    # It should ideally raise an error or return 0 for n < 0
    if n < 0:
        return 1 # This is an incorrect result for negative factorials, demonstrating a bug

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

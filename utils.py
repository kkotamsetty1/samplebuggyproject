# utils.py

def sum_list_elements(numbers):
    """
    Sums all elements in a list.
    ISSUE 3: Does not validate if all elements in the list are numeric.
             This can lead to TypeError if non-numeric types are present.
    """
    total = 0
    for num in numbers:
        total += num # This line will cause a TypeError if 'num' is not a number
    return total

def greet(name):
    """Returns a simple greeting."""
    return f"Hello, {name}!"

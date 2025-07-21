# main.py

from calculator import add, subtract, multiply, divide, factorial
from utils import sum_list_elements

def run_calculator_demos():
    print("--- Calculator Demos ---")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")

    # --- Intended Bug 1: Division by Zero ---
    print("\nAttempting division by zero (expected error):")
    print(f"8 / 0 = {divide(8, 0)}") # This line will cause an error

    # --- Intended Bug 2: Factorial for negative number ---
    print("\nAttempting factorial for negative number (expected incorrect behavior/error):")
    print(f"Factorial of -5 = {factorial(-5)}") # This might return 1 or raise an error

    # --- Inefficiency 1: Factorial is simple and could be optimized for large numbers ---
    print("\nFactorial of 5 (basic implementation):")
    print(f"Factorial of 5 = {factorial(5)}")

def run_utility_demos():
    print("\n--- Utility Demos ---")
    my_numbers = [10, 20, 30, 40]
    print(f"Sum of {my_numbers} = {sum_list_elements(my_numbers)}")

    # --- Intended Bug 3: Non-numeric elements in list ---
    print("\nAttempting to sum list with non-numeric elements (expected error):")
    mixed_list = [1, 2, 'three', 4]
    print(f"Sum of {mixed_list} = {sum_list_elements(mixed_list)}") # This line will cause an error

if __name__ == "__main__":
    run_calculator_demos()
    print("\n" + "="*30 + "\n")
    run_utility_demos()

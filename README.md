Simple Python Demo Project
This is a small Python project designed to demonstrate basic functionality and highlight a few common coding issues that an AI agent like Jules could help fix.

Project Structure
main.py: Entry point to run various calculator and utility demos.

calculator.py: Contains basic arithmetic functions (add, subtract, multiply, divide) and a factorial function.

utils.py: Contains utility functions, currently just one for summing list elements.

tests/: Directory for unit tests (currently sparse).

requirements.txt: Project dependencies.

Known Issues (for AI Agent Demonstration)
calculator.py - Division by Zero: The divide function does not handle division by zero gracefully, leading to a runtime error.

calculator.py - Factorial for Negative Numbers: The factorial function provides an incorrect result (returns 1) for negative input, where it should ideally raise an error or return 0.

calculator.py - Factorial Inefficiency: The factorial implementation is a basic loop and could be optimized for very large numbers.

utils.py - Non-Numeric Sum: The sum_list_elements function does not validate input types and will raise a TypeError if non-numeric values are passed in the list.

Missing Tests: The tests/test_calculator.py file is largely empty, indicating a lack of comprehensive unit tests for the calculator.py module.

How to Run
Clone this repository.

(Optional) Create a virtual environment: python3 -m venv venv

(Optional) Activate the virtual environment:

macOS/Linux: source venv/bin/activate

Windows: .\venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run the main application: python main.py

Observe the errors and inefficiencies as you run main.py.

"""
This script provides functions to calculate the type of triangle based on the side lengths. 
It includes validation for valid triangle side lengths, and identifies whether the triangle is Equilateral, Isosceles, or Scalene.

Functions:
- is_called_from_pytest: Detrmines if script is executed from pytest.
- triangle_type: Determines the triangle type based on side lengths.
- is_valid_triangle: Checks if the given side lengths form a valid triangle.
- validate_inputs: Validates and converts inputs to float.
- ask_user_inputs: Asks user input.
"""

import sys

def is_called_from_pytest():
    """
    Helper to validate if this is a test run or not
    """
    return 'pytest' in sys.argv[0] or __name__ == 'pytest'


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    Check if three sides can form a triangle
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def triangle_type(a, b, c) -> str:
    """
    Determine the type of triangle
    """
    # Validate and preprocess the inputs
    validated = validate_inputs(a, b, c)
    if validated is None:  # If validation fails
        return "Invalid input"

    # Unpack the validated side lengths
    a, b, c = validated

    if not is_valid_triangle(a, b, c):
        return "The given values do not form a triangle."
    if a == b == c:
        return "The triangle is Equilateral."
    elif a == b or b == c or a == c:
        return "The triangle is Isosceles."
    else:
        return "The triangle is Scalene."


def validate_inputs(a, b, c):
    """
    Validate inputs
    """
    try:
        # Get inputs and trim whitespace (strings)
        # Ensure the values are strings, so strip and replace work
        if isinstance(a, str):
            a = a.strip().replace(',', '.')
        if isinstance(b, str):
            b = b.strip().replace(',', '.')
        if isinstance(c, str):
            c = c.strip().replace(',', '.')

        # Convert inputs to floats for numeric operations
        a = float(a)
        b = float(b)
        c = float(c)

        # Check for non-positive values
        if a <= 0 or b <= 0 or c <= 0:
            print("Side lengths must be positive numbers greater than 0")
            return None

        return a, b, c

    except ValueError:
        print("Please, enter valid numeric values for all sides (scientific notation is also accepted - 1e2, 2.5e-1, etc.)")
        return None


def ask_user_inputs():
    """
    Ask user inputs
    """
    # Get inputs
    a = input("Enter side a: ")
    b = input("Enter side b: ")
    c = input("Enter side c: ")
    return triangle_type(a, b, c)


# Ask for inputs if this is not a test run
if not is_called_from_pytest():
    print("No a test run")
    print(ask_user_inputs())

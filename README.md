# Triangle Type Checker

This Python script provides functions to determine the type of a triangle based on the side lengths. It includes validation to ensure the side lengths form a valid triangle and identifies whether the triangle is Equilateral, Isosceles, or Scalene.

## Features

- **Validation**: Ensures that the side lengths are valid numbers and that they can form a triangle.
- **Triangle Type Identification**: Determines whether the triangle is Equilateral, Isosceles, or Scalene based on the side lengths.
- **Scientific Notation Support**: Handles side lengths provided in scientific notation (e.g., `1e2` or `2.5e-1`).
- **Command-line and Test Support**: Includes functionality to ask user inputs or be used in a test environment (via `pytest`).

## Functions

### `is_called_from_pytest()`

Helper function to determine if the script is executed from `pytest`. This allows the script to handle testing and user interaction appropriately.

### `triangle_type(a, b, c) -> str`

Determines the type of triangle based on the side lengths:

- **Equilateral**: All sides are equal.
- **Isosceles**: Two sides are equal.
- **Scalene**: All sides are different.

### `is_valid_triangle(a: float, b: float, c: float) -> bool`

Checks if the three given side lengths form a valid triangle based on the triangle inequality theorem. The sum of the lengths of any two sides must be greater than the length of the third side.

### `validate_inputs(a, b, c)`

Validates and converts input values into floats. It also checks for non-positive values and ensures the inputs are valid numbers.

### `ask_user_inputs()`

Prompts the user for side lengths and returns the type of triangle based on the entered values.

## Installation

### Clone the repository

```bash
[git clone [https://github.com/your-username/triangle-type-checker.git](https://github.com/jur4x/triangle_tester.git)]

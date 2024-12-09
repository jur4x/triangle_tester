import pytest
import sys
from triangle import triangle_type

#Test for valid triangle types
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (3, 4, 5, "The triangle is Scalene."),  # Scalene triangle
        (5, 5, 5, "The triangle is Equilateral."),  # Equilateral triangle
        (5, 5, 8, "The triangle is Isosceles."),  # Isosceles triangle
        (8, 5, 5, "The triangle is Isosceles."),  # Isosceles triangle (sides in different order)
    ]
)
def test_valid_triangles(a, b, c, expected_result):
    """Test valid triangle types."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"
    

#Test for invalid triangles
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (1, 1, 3, "The given values do not form a triangle."),  # Imposible triangle
        (2, 2, 5, "The given values do not form a triangle."),  # Imposible triangle
        (10, 2, 5, "The given values do not form a triangle.")  # Imposible triangle
    ]
)
def test_invalid_triangles(a, b, c, expected_result):
    """Test invalid triangles."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"
    

# Degenerate triangle (sum of two sides equals the third)
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (1, 2, 3, "The given values do not form a triangle.") # Degenerate triangle
    ]
)
def test_degenerate_triangle(a, b, c, expected_result):
    """Test degenerate triangle where sum of two sides equals the third."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"


#Test for invalid inputs (non-numeric or negative or 0 values)
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        ("a", 4, 5, "Invalid input"),   # Non-numeric value
        (1, 1, 0, "Invalid input"),   # Zero value
        (5, 4, -5, "Invalid input"),   # Negative side length
        ("", 4, 5, "Invalid input"),   # Empty string for side
    ]
)
def test_invalid_inputs(a, b, c, expected_result):
    """Test invalid inputs."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"
    

#Test for input with commas (checking replacement of commas with dots)
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        ("3,0", "4,0", "5,0", "The triangle is Scalene."),  # Comma in string, should be converted to dot
        ("5,5", "5,5", "5,5", "The triangle is Equilateral.")  # Comma in string, should be converted to dot
    ]
)
def test_input_with_commas(a, b, c, expected_result):
    """Test inputs with commas, should handle correctly."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"
    

#Test for input with commas (checking replacement of commas with dots) mixed with dots
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        ("3,0", "4.0", "5,0", "The triangle is Scalene."),  # Comma in string, should be converted to dot
        ("5.5", "5,5", "5.5", "The triangle is Equilateral.")  # Comma in string, should be converted to dot
    ]
)
def test_input_with_commas_and_dots(a, b, c, expected_result):
    """Test inputs with commas and dots mixed, should handle correctly."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"


#Test for scientific inputs
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        ("1e2", "1e2", "1e2", "The triangle is Equilateral."),
        ("2.5e-1", "2.5e-1", "2.5e-1", "The triangle is Equilateral.")
    ]
)
def test_scientific_notation_inputs(a, b, c, expected_result):
    """Test scientific notation inputs, should be handled correctly."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"


#Test for maximum float values
@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (sys.float_info.max, sys.float_info.max, sys.float_info.max, "The triangle is Equilateral."),  # Max float values, expected Equilateral triangle
    ]
)
def test_max_float_values(a, b, c, expected_result):
    """Test the largest representable float values."""
    result = triangle_type(a, b, c)
    assert result == expected_result, f"Expected '{expected_result}' but got '{result}' with a={a}, b={b}, c={c}"

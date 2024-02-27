import pytest
from Practice_code.recursion.factorial import factorial

# Test case for factorial of 0
def test_factorial_of_0():
    assert factorial(0) == 1

# Test case for factorial of positive numbers
@pytest.mark.parametrize("n, expected", [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)])
def test_factorial_of_positive_numbers(n, expected):
    assert factorial(n) == expected

# Test case for factorial of negative numbers
def test_factorial_of_negative_numbers():
    with pytest.raises(ValueError):
        factorial(-1)

# Test case for factorial of non-integer input
def test_factorial_of_non_integer():
    with pytest.raises(TypeError):
        factorial(1.5)

# # Test case for factorial of large numbers
# def test_factorial_of_large_numbers():
#     assert factorial(20) == 2432902008176640000
#     assert factorial(50) == 30414093201713378043612608166064768844377641568960512000000000000

if __name__ == "__main__":
    pytest.main()
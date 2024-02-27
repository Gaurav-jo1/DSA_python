import pytest
from Practice_code.recursion.fibonacci import fibonacci

# Test case to find the Fibonacci number at index 5
def test_fibonacci_at_index_5():
    assert fibonacci(5) == 5

# Test case to find the Fibonacci number at index 10
def test_fibonacci_at_index_10():
    assert fibonacci(10) == 55

# Test case to find the Fibonacci number at index 20
def test_fibonacci_at_index_20():
    assert fibonacci(20) == 6765


# Fibonacci Series Test
from Practice_code.recursion.fibonacci import fibonacci_series
# Test case for generating first 0 Fibonacci numbers
def test_fibonacci_series_with_zero_numbers():
    assert fibonacci_series(0) == []

# Test case for generating first 1 Fibonacci number
def test_fibonacci_series_with_one_number():
    assert fibonacci_series(1) == [0]

# Test case for generating first 2 Fibonacci numbers
def test_fibonacci_series_with_two_numbers():
    assert fibonacci_series(2) == [0, 1]

# Test case for generating first 5 Fibonacci numbers
def test_fibonacci_series_with_five_numbers():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]

# Test case for generating first 10 Fibonacci numbers
def test_fibonacci_series_with_ten_numbers():
    assert fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Test case for generating first 15 Fibonacci numbers
def test_fibonacci_series_with_fifteen_numbers():
    assert fibonacci_series(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# Test case for generating first 20 Fibonacci numbers
def test_fibonacci_series_with_twenty_numbers():
    assert fibonacci_series(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# # Test case for generating first 30 Fibonacci numbers
# def test_fibonacci_series_with_thirty_numbers():
#     assert fibonacci_series(30) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]

# # Test case for generating first 50 Fibonacci numbers
# def test_fibonacci_series_with_fifty_numbers():
#     assert fibonacci_series(50) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]
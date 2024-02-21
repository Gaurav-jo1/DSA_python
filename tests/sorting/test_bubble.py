import pytest
from Practice_code.sorting.bubble_sort import bubble_sort

# Test case for an empty list
def test_empty_list():
    assert bubble_sort([]) == []

# Test case for a list with one element
def test_one_element():
    assert bubble_sort([5]) == [5]

# Test case for a list with multiple elements in ascending order
def test_ascending_order():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test case for a list with multiple elements in descending order
def test_descending_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# Test case for a list with multiple elements in random order
def test_random_order():
    assert bubble_sort([3, 5, 1, 4, 2]) == [1, 2, 3, 4, 5]

# Test case for a list with duplicate elements
def test_duplicate_elements():
    assert bubble_sort([3, 5, 1, 4, 2, 3, 1, 2]) == [1, 1, 2, 2, 3, 3, 4, 5]

# Test case for a list with negative numbers
def test_negative_numbers():
    assert bubble_sort([-3, -5, -1, -4, -2]) == [-5, -4, -3, -2, -1]

# Test case for a list with mixed positive and negative numbers
def test_mixed_numbers():
    assert bubble_sort([-3, 5, -1, 4, 0, -2]) == [-3, -2, -1, 0, 4, 5]

# Test case for a large list
def test_large_list():
    assert bubble_sort(list(range(10000, 0, -1))) == list(range(1, 10001))

# Test case for a list with strings
def test_strings():
    assert bubble_sort(['banana', 'apple', 'orange', 'grape']) == ['apple', 'banana', 'grape', 'orange']

# Test case for a list with mixed types
def test_mixed_types():
    with pytest.raises(TypeError):
        bubble_sort([1, 'apple', 3, 'banana'])

# Test case for sorting an already sorted list
def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    pytest.main()
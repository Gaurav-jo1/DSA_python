import pytest
from Practice_code.sorting.insertion_sort import insertion_sort

def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []

def test_insertion_sort_sorted_list():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted_list():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_insertion_sort_unsorted_list():
    assert insertion_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]

def test_insertion_sort_with_duplicates():
    assert insertion_sort([3, 1, 4, 2, 5, 3, 2]) == [1, 2, 2, 3, 3, 4, 5]

def test_insertion_sort_with_negative_numbers():
    assert insertion_sort([-3, -1, -4, -2, -5]) == [-5, -4, -3, -2, -1]

def test_insertion_sort_with_mixed_numbers():
    assert insertion_sort([3, -1, 4, -2, 0, 5]) == [-2, -1, 0, 3, 4, 5]
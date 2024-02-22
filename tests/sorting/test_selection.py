import pytest
from Practice_code.sorting.selection_sort import selection_sort

def test_selection_sort_empty_list():
    assert selection_sort([]) == []

def test_selection_sort_sorted_list():
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_selection_sort_reverse_sorted_list():
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_selection_sort_random_list():
    assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_selection_sort_with_duplicates():
    assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 4, 4]) == [1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 9]

def test_selection_sort_with_negative_numbers():
    assert selection_sort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3]) == [-9, -6, -5, -5, -4, -3, -3, -2, -1, -1]

def test_selection_sort_with_mixed_numbers():
    assert selection_sort([-3, 1, -4, 0, 5, -9, 2, 6, -5, 3,]) == [-9, -5, -4, -3, 0, 1, 2, 3, 5, 6]

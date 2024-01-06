# test_binary_search.py
import pytest
from _1_Binary_search.basic import b_search


def test_binary_search():
    # Test case 1: Target is present in the middle of the array
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target1 = 5
    assert b_search(arr1, target1) == 4

    # Test case 2: Target is the first element of the array
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target2 = 1
    assert b_search(arr2, target2) == 0

    # Test case 3: Target is the last element of the array
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target3 = 9
    assert b_search(arr3, target3) == 8

    # Test case 4: Target is not present in the array
    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target4 = 10
    assert b_search(arr4, target4) == -1

    # Test case 5: Empty array
    arr5 = []
    target5 = 5
    assert b_search(arr5, target5) == -1

    # Test case 6: Array with one element (target present)
    arr6 = [5]
    target6 = 5
    assert b_search(arr6, target6) == 0

    # Test case 7: Array with one element (target not present)
    arr7 = [3]
    target7 = 5
    assert b_search(arr7, target7) == -1


from _1_Binary_search.basic import find_ceiling

def test_ceiling_in_array():
    arr = [1, 2, 8, 10, 10, 12, 19]
    target = 5
    assert find_ceiling(arr, target) == 8

def test_ceiling_not_in_array():
    arr = [1, 2, 8, 10, 10, 12, 19]
    target = 20
    assert find_ceiling(arr, target) is None

def test_empty_array():
    arr = []
    target = 5
    assert find_ceiling(arr, target) is None

def test_ceiling_at_beginning():
    arr = [1, 2, 8, 10, 10, 12, 19]
    target = 0
    assert find_ceiling(arr, target) == 1

def test_ceiling_at_end():
    arr = [1, 2, 8, 10, 10, 12, 19]
    target = 25
    assert find_ceiling(arr, target) is None


if __name__ == "__main__":
    pytest.main()


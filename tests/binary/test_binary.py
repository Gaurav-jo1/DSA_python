# test_binary_search.py
import pytest
from Practice_code.binary.binary import b_search


def test_binary_search():
    # Test case 1: Target found in the middle of the array
    arr1 = [1, 3, 5, 7, 9]
    target1 = 5
    assert b_search(arr1, target1) == 2

    # Test case 2: Target found at the beginning of the array
    arr2 = [1, 3, 5, 7, 9]
    target2 = 1
    assert b_search(arr2, target2) == 0

    # Test case 3: Target found at the end of the array
    arr3 = [1, 3, 5, 7, 9]
    target3 = 9
    assert b_search(arr3, target3) == 4

    # Test case 4: Target not found in the array
    arr4 = [1, 3, 5, 7, 9]
    target4 = 4
    assert b_search(arr4, target4) == -1

    # Test case 5: Empty array
    arr5 = []
    target5 = 5
    assert b_search(arr5, target5) == -1

    # Test case 6: None target
    arr6 = [1, 3, 5, 7, 9]
    target6 = None
    assert b_search(arr6, target6) == -1


from Practice_code.binary.binary import ceiling

def test_ceiling():
    # Test case 1: Target is smaller than all elements in the array
    arr1 = [5, 10, 15, 20]
    target1 = 3
    assert ceiling(arr1, target1) == 5

    # Test case 2: Target is equal to an element in the array
    arr2 = [5, 10, 15, 20]
    target2 = 10
    assert ceiling(arr2, target2) == 10

    # Test case 3: Target is between two elements in the array
    arr3 = [5, 10, 15, 20]
    target3 = 12
    assert ceiling(arr3, target3) == 15

    # Test case 4: Target is larger than all elements in the array
    arr4 = [5, 10, 15, 20]
    target4 = 25
    assert ceiling(arr4, target4) == None

    # Test case 5: Empty array
    arr5 = []
    target5 = 10
    assert ceiling(arr5, target5) == None

    # Test case 6: None target
    arr6 = [5, 10, 15, 20]
    target6 = None
    assert ceiling(arr6, target6) == None


from Practice_code.binary.binary import floor

# Pytest function to test floor function
def test_floor():
    # Test case 1: Target is smaller than all elements in the array
    arr1 = [5, 10, 15, 20]
    target1 = 3
    assert floor(arr1, target1) == None

    # Test case 2: Target is equal to an element in the array
    arr2 = [5, 10, 15, 20]
    target2 = 10
    assert floor(arr2, target2) == 10

    # Test case 3: Target is between two elements in the array
    arr3 = [5, 10, 15, 20]
    target3 = 12
    assert floor(arr3, target3) == 10

    # Test case 4: Target is larger than all elements in the array
    arr4 = [5, 10, 15, 20]
    target4 = 25
    assert floor(arr4, target4) == 20

    # Test case 5: Empty array
    arr5 = []
    target5 = 10
    assert floor(arr5, target5) == None

    # Test case 6: None target
    arr6 = [5, 10, 15, 20]
    target6 = None
    assert floor(arr6, target6) == None

# Run the test function with pytest
if __name__ == "__main__":
    pytest.main()

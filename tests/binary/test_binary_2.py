import pytest
from Practice_code.binary.binary_2d import binary_search_2d

@pytest.fixture
def sorted_2d_array():
    return [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]

def test_binary_search_2d_found(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 9) == (1, 1)

def test_binary_search_2d_not_found(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 8) == (-1, -1)

def test_binary_search_2d_first_element(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 1) == (0, 0)

def test_binary_search_2d_last_element(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 17) == (2, 2)

def test_binary_search_2d_corner_case_upper_left(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 3) == (0, 1)

def test_binary_search_2d_corner_case_upper_right(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 5) == (0, 2)

def test_binary_search_2d_corner_case_lower_left(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 13) == (2, 0)

def test_binary_search_2d_corner_case_lower_right(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 15) == (2, 1)

def test_binary_search_2d_element_in_first_column(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 7) == (1, 0)

def test_binary_search_2d_element_in_last_column(sorted_2d_array):
    assert binary_search_2d(sorted_2d_array, 11) == (1, 2)


# Run the test function with pytest
if __name__ == "__main__":
    pytest.main()
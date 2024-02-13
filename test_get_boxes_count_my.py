import pytest
from get_boxes_count_my import get_boxes_count

@pytest.mark.parametrize(['products_count', 'box_capacity', 'expected_value'], # parametrization
[
 # Positive
 (10, 5, 2),
 (12, 5, 3),
 (4, 5, 1),
 (5, 10, 1),
 (1, 5, 1),
 (1, 1, 1),
 (999, 1000, 1),
 (999999999, 1000000000, 1),
 ])
def tests_positive(products_count, box_capacity, expected_value):
    assert get_boxes_count(products_count, box_capacity) == expected_value

@pytest.mark.parametrize(['products_count', 'box_capacity', 'error'], # parametrization
[
 # Negative
 ("A", 6, AssertionError), # Value unacceptable
 (6, "A", AssertionError), # Value unacceptable
 (1.3, 6, AssertionError), # Value unacceptable
 (6, 1.3, AssertionError), # Value unacceptable
 (9, 0, AssertionError), # Value unacceptable
 (0, 9, AssertionError), # Value unacceptable
 (0, 0, AssertionError), # Value unacceptable
 (-3, 6, AssertionError), # Value unacceptable
 (2, -2, AssertionError), # Value unacceptable
 ([], None, AssertionError), # Value unacceptable
 (None, [], AssertionError), # Value unacceptable
 ((1, 2), {1: '11'}, AssertionError), # Value unacceptable
 ([1, 2], {1, 2, 3}, AssertionError), # Value unacceptable
])

def test_negative(products_count, box_capacity, error):
    with pytest.raises(error): # with-context manager
        get_boxes_count(products_count, box_capacity)



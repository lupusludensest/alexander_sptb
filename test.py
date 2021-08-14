import pytest
from function import get_boxes_count

@pytest.mark.parametrize(['products_count', 'box_capacity', 'error'],
[
 # Negative
 ("A", 6, ValueError),
 (6, "A", ValueError),
 (1.3, 6, ValueError),
 (6, 1.3, ValueError),
 (9, 0, ValueError),
 (0, 9, ValueError),
 (0, 0, ValueError),
 (-3, 6, ValueError),
 (2, -2, ValueError),
 ([], None, ValueError),
 (None, [], ValueError),
 ((1, 2), {1: '11'}, ValueError),
 ([1, 2], {1, 2, 3}, ValueError),
])

def test_negative(products_count, box_capacity, error):
    with pytest.raises(error):
        get_boxes_count(products_count, box_capacity)

@pytest.mark.parametrize(['products_count', 'box_capacity', 'expected_value'],
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

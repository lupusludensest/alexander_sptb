import pytest
from boxes_count import get_boxes_count


@pytest.mark.parametrize(['products_count', 'box_capacity', 'error'],
                         [
                             # Negative
                             ("A", 6, TypeError),
                             (1.3, 6, TypeError),
                             (9, 0, ZeroDivisionError),
                             (-3, 6, ValueError),
                             (2, -2, ValueError),
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
                             (0, 5, 0),
                         ])
def tests_positive(products_count, box_capacity, expected_value):
    assert get_boxes_count(products_count, box_capacity) == expected_value

# to run this use command pytest -s -v test_signature.py

import pytest
from function_signature import get_boxes_count

@pytest.mark.parametrize(['quantity', 'in_box', 'you_need_boxes'],
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
def tests_positive(quantity, in_box, you_need_boxes):
    assert get_boxes_count(quantity, in_box) == str(you_need_boxes)

@pytest.mark.parametrize(['quantity', 'in_box', 'error'],
[
 # Negative
 ("A", 6, AssertionError), # Value unacceptable
 (6, "A", AssertionError), # Value unacceptable
 (1.3, 6, AssertionError), # Value unacceptable
 (6, 1.3, AssertionError), # Value unacceptable
 (9, 0, AssertionError), # Value unacceptable
 (0, 9, AssertionError), # Value unacceptable
 (0, 0, AssertionError), # Value unacceptable
 (-3, 6,AssertionError), # Value unacceptable
 (2, -2, AssertionError), # Value unacceptable
 ([], None, AssertionError), # Value unacceptable
 (None, [], AssertionError), # Value unacceptable
 ((1, 2), {1: '11'}, AssertionError), # Value unacceptable
 ([1, 2], {1, 2, 3}, AssertionError), # Value unacceptable
])

def test_negative(quantity, in_box, error):
    with pytest.raises(error):
        get_boxes_count(quantity, in_box)

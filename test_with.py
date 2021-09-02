import pytest

from get_boxes_count import get_boxes_count


def test_wrong_input_type_string():
    with pytest.raises(TypeError): # with-context manager
        get_boxes_count("A", 6)


def test_wrong_input_type_float():
    with pytest.raises(TypeError): # with-context manager
        get_boxes_count(1.3, 6)


def test_wrong_input_type_zero():
    with pytest.raises(ZeroDivisionError): # with-context manager
        get_boxes_count(9, 0)


def test_wrong_input_negative_product():
    with pytest.raises(ValueError): # with-context manager
        get_boxes_count(-3, 6)


def test_wrong_input_negative_capacity():
    with pytest.raises(ValueError): # with-context manager
        get_boxes_count(2, -2)


def test_positive_int_equal():
    assert get_boxes_count(10, 5) == 2


def test_positive_int_not_equal():
    assert get_boxes_count(12, 5) == 3


def test_less_one_box():
    assert get_boxes_count(4, 5) == 1


def test_zero_product():
    assert get_boxes_count(0, 5) == 0
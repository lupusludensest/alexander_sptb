import math


def get_boxes_count(products_count, box_capacity):
    # Check if the input data are correct
    if type(products_count) != int or type(box_capacity) != int:
        raise TypeError('The input data should be integer')
    if products_count < 0 or box_capacity < 0:
        raise ValueError('The input data should be positive')
    if box_capacity == 0:
        raise ZeroDivisionError('Zero division error, box_capacity should be non zero')
    return math.ceil(products_count/box_capacity)

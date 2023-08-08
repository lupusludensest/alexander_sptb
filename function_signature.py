# Тестовое задание
# Нужно написать реализацию функции, которая будет принимать на вход два аргумента:
# - количество продуктов которое нужно отправить
# - количество продуктов которое помещается в коробку
# Возвращает одно целочисленное значение
# - количество коробок для всех недопустимых значений на входе функция должна возвращать AssertionError.
# Как результат хочется получить два файла:
# 1. файл с функцией
# 2. файл с тестами на эту функцию
# Тесты должны быть написаны для pytest, с параметризацией. Хочется видеть позитивные и негативные кейсы.
# Ожидаем использование python 3.5+Пример сигнатуры функции
# def get_boxes_count(products_count, box_capacity):

import math
import typing

product_count = int(input('Enter the product quantity: '))
box_capacity = int(input('Enter the boxes capacity: '))
def get_boxes_count(products_count: int, box_capacity: int) -> int: # signature
    # Check if the input data are correct
    if type(products_count) != int or type(box_capacity) != int or products_count < 1 or box_capacity < 1:
        raise AssertionError('AssertionError') # Value unacceptable
    return f'{math.ceil(products_count/box_capacity)}' # returns the result

print(get_boxes_count(product_count, box_capacity))

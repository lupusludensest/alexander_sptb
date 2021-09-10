# Тестовое задание
# Нужно написать реализацию функции, которая будет принимать на вход два аргумента:
# - количество продуктов которое нужно отправить
# - количество продуктов которое помещается в коробку
# Возвращает одно целочисленное значение
# - количество коробокДля всех недопустимых значений на входе функция должна возвращать AssertionError.
# Как результат хочется получить два файла:
# 1. файл с функцией
# 2. файл с тестами на эту функцию
# Тесты должны быть написаны для pytest, с параметризацией. Хочется видеть позитивные и негативные кейсы.
# Ожидаем использование python 3.5+Пример сигнатуры функции
# def get_boxes_count(products_count, box_capacity):

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

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

products_count, box_capacity = input('Enter the product quantity: '), input('Enter the box capacity: ')
def get_boxes_count(products_count, box_capacity) -> int:
    prdcts_cnt_int = int(products_count)
    bx_cpcty_int = int(box_capacity)
    print(type(products_count), type(box_capacity), type(prdcts_cnt_int), type(bx_cpcty_int))
    if (type(prdcts_cnt_int)!=int or type(bx_cpcty_int)!=int or len(str(prdcts_cnt_int))==0 or len(str(bx_cpcty_int))==0 or bx_cpcty_int==0 or prdcts_cnt_int==0):
        return 'AssertionError'
    if type(prdcts_cnt_int)==int and type(bx_cpcty_int)==int:
        return f'We need "{math.ceil(int(prdcts_cnt_int)/int(bx_cpcty_int))}" boxes'
    else:
        return 'AssertionError'

print(get_boxes_count(products_count, box_capacity))





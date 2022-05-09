"""
Please write a function that gets a list as an 
input parameter and returns another list as output.

Every element of the output list is a product of all 
the elements of input list except the element at the 
current index position in the input list.
"""

"""
There are two different solutions. The time complexity of both of them is O(N*N).
It is possible to change the algorithm and makes it O(N), if it is nessesary.
For that additional information is needed:  
What is the maximum length of the input list?
What is the data in the list? float? integer? What is the maximum for elements of the list?

I suppose that the input list is the list of integers. 
"""

import math
import pytest

# Most simple solution which doesn't use libraries. 
def product_list(lst):
	# Check if the input data are correct
	if type(lst) != list:
		raise TypeError("The input data should be a list type")
	for x in lst:
		if type(x) != int:
			raise TypeError("The input data should be a list of integers.")	
	# Assign a new list for output data
	new_lst = []
	# Calculating product for each list element and put it to new_lst
	for i in range(len(lst)):
		prod = 1
		for j in range(len(lst)):
			if i != j:
				prod *= lst[j]
		new_lst.append(prod)
	return new_lst			

# The short code using list comprehension and math library. 
def product_list_short_code(lst):
	#Check if the input data are correct
	if type(lst) != list:
		raise TypeError("The input data should be a list type")
	for x in lst:
		if type(x) != int:
			raise TypeError("The input data should be a list of integers.")	
	# Calculate product for each element using math library and list comprehension
	return [math.prod(lst[:i] + lst[i + 1:]) for i in range(len(lst))]


lst = []
print(product_list(lst))  # []
print(product_list_short_code(lst))  # []

lst = [1, 4, 5, 7, 9, 4, 2]
print(product_list(lst))  # [10080, 2520, 2016, 1440, 1120, 2520, 5040]
print(product_list_short_code(lst))  # [10080, 2520, 2016, 1440, 1120, 2520, 5040]

lst = [1, -4, 5, 7, -9, 4, 2]
print(product_list(lst))   # [10080, -2520, 2016, 1440, -1120, 2520, 5040]
print(product_list_short_code(lst))   # [10080, -2520, 2016, 1440, -1120, 2520, 5040]

lst = [0, 4, 5, 7, 9, 4, 2]
print(product_list(lst))  # [10080, 0, 0, 0, 0, 0, 0]
print(product_list_short_code(lst))  # [10080, 0, 0, 0, 0, 0, 0]

lst = [1, 4, 5, 0, 9, 0, 2]
print(product_list(lst))   #  [0, 0, 0, 0, 0, 0, 0]
print(product_list_short_code(lst))   #  [0, 0, 0, 0, 0, 0, 0]

# Tests to check functionality for both function:

def test_wrong_input_type():
    with pytest.raises(TypeError): # context manager
        product_list("A")

def test_wrong_input_type_short():
    with pytest.raises(TypeError): # context manager
        product_list_short_code("A")

def test_wrong_input_list_elements_type():
    with pytest.raises(TypeError): # context manager
        product_list([1, 3, "4"])        

def test_wrong_input_list_elements_type_short():
    with pytest.raises(TypeError): # context manager
        product_list_short_code([1, 3, "4"])        

def test_empty_list():
    assert product_list([]) == []

def test_empty_list_short():
    assert product_list_short_code([]) == []    

def test_positive_integers():
    assert product_list([1, 4, 5, 7, 9, 4, 2]) == [10080, 2520, 2016, 1440, 1120, 2520, 5040]

def test_positive_integers_short():
    assert product_list_short_code([1, 4, 5, 7, 9, 4, 2]) == [10080, 2520, 2016, 1440, 1120, 2520, 5040]    

def test_negative_integers():
    assert product_list([1, -4, 5, 7, -9, 4, 2]) == [10080, -2520, 2016, 1440, -1120, 2520, 5040]

def test_negative_integers_short():
    assert product_list_short_code([1, -4, 5, 7, -9, 4, 2]) == [10080, -2520, 2016, 1440, -1120, 2520, 5040]

def test_one_zero():
    assert product_list([0, 4, 5, 7, 9, 4, 2]) == [10080, 0, 0, 0, 0, 0, 0]

def test_one_zero_short():
    assert product_list_short_code([0, 4, 5, 7, 9, 4, 2]) == [10080, 0, 0, 0, 0, 0, 0]

def test_two_zero():
    assert product_list([0, 4, 5, 0, 9, 4, 2]) == [0, 0, 0, 0, 0, 0, 0]

def test_two_zero_short():
    assert product_list_short_code([0, 4, 5, 0, 9, 4, 2]) == [0, 0, 0, 0, 0, 0, 0]    

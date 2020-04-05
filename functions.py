import pandas as pd
import numpy as np

arr = [1,2,3]
matr = [[1,2,3], [4,5,6]]

sq_length = 4
sq_width = 4

rect_length = 8
rect_width = 5

def area(length, width):
    '''Returns the area of a square or rectangle in units squared'''
    area = length * width
    print(f'Area of the shape = {area}')

check_it = area(length=rect_length, width=rect_width)
check_it

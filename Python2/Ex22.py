from math import *

length1 = float(input('please enter the length of the first side'))
length2 = float(input('please enter the length of the second side'))
length3 = float(input('please enter the length of the third side'))

length_sum = length1 + length2 + length3
area = sqrt(length_sum*(length_sum-length1)*(length_sum-length2)*(length_sum-length3))
print(f'the area of the triangle is {area}')
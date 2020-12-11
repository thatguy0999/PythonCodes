from math import *

length = float(input('please enter the length of one side'))
no_sides = int(input('please enter the sides of the polygon'))

print(f'the area of the polygon is {(no_sides*length**2)/(4*tan(pi/no_sides)):.2f}')
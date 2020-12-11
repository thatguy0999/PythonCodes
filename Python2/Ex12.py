from math import *

x_coord_1 = (int(input('what is the x coordinate of the first point: ')))
y_coord_1 = (int(input('what is the y coordinate of the first point: ')))
x_coord_2 = (int(input('what is the x coordinate of the second point: ')))
y_coord_2 = (int(input('what is the y coordinate of the second point: ')))

distance = abs(6371.01*acos(sin(x_coord_1))*sin(x_coord_2) + cos(x_coord_1)*cos(x_coord_1)*cos(y_coord_1-y_coord_2))

print(f'The distance between these two points are {distance}')

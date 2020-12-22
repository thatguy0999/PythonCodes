from math import sqrt

re = 0
total_dist = 0

while True:
    coord = input('please enter the coordinates of the point  ')
    if coord == '':
        break

    else:
        x,y = coord.split(',')
        x = int(x)
        y = int(y)
        if re == 0:
            point_1 = x
            point_2 = y
            prev_x = x
            prev_y = y

        else:
            total_dist += sqrt((x - prev_x)**2 + (y - prev_y)**2)
            prev_x = x
            prev_y = y
            
    re += 1

if re == 0 or re == 1 or re == 2:
    print('not a valid polygon')

else:
    total_dist += sqrt((point_1 - x)**2 + (point_2 - prev_y)**2)
    print(f'the perimeter is {total_dist:.3f}')
from math import sqrt

while True:
    side_1 = float(input('enter the length of the first side'))
    side_2 = float(input('enter the length of the second side'))
    side_3 = float(input('enter the length of the third side'))

    if (side_1 + side_2) > side_3 and (side_1 + side_3) > side_2 and (side_2 + side_3) > side_1:
        if side_1 == side_2 == side_3:
            print('the triangle is an equilateral')
            break

        elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
            print('the triangle is an isosceles')
            break

        else:
            print('the triangle is scalene')
            break
    else:
        print('invalid triangle')
    
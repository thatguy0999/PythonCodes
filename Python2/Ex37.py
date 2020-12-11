# while True:
#     sides = input('enter the number of sides on a polygon')
#     try:
#         sides = int(sides)
#         if sides < 3 or sides > 10:
#             print('we do not accept shapes within this range')

#         elif sides == 3:
#             print('triangle')
#             break

#         elif sides == 4:
#             print('quadrilateral')
#             break

#         elif sides == 5:
#             print('pentagon')
#             break

#         elif sides == 6:
#             print('hexagon')
#             break

#         elif sides == 7:
#             print('heptagon')
#             break

#         elif sides == 8: 
#             print('octagon')
#             break

#         elif sides == 9:
#             print('nonagon')
#             break

#         elif sides == 10:
#             print('decagon')
#             break

#     except:
#         print('please enter a valid input')

shapes = ['triangle','quadtrilateral','pentagon','hexagon','heptagon','octagon','nonagon','decagon']

while True:
    sides = input('enter the number of sides on a polygon')
    try:
        sides = int(sides)
        if sides < 3 or sides > 10:
            print('we do not accept shapes within this range')

        else:
            print(shapes[sides-3])
            break

    except:
        print('please enter a valid input')

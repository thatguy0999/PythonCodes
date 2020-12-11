from math import pi

radius = float(input('what is the radius of the circle/sphere (cm)'))

print(f'''
The circle's area is {pi*radius**2:.3f} cm^2
The sphere's area is {(4/3)*pi*radius**3:.3f} cm^3
''')
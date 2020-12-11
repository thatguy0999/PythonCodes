feet = float(input('How many feet'))

miles = feet/5280
feet %= 5280
yards = feet/3
feet %= 3
inches = feet*12

print(f'''
The distance is
{miles:.2f} miles
{yards} yards
and {inches} inches
''')
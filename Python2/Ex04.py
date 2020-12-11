width = input('what is the width of the field? (in feet)')
length = input('what is the length of the field? (in feet)')

area = float(width)*float(length)
# 1a = 43,560f^2
area_acres = area/43560
print( area_acres, 'acres')
from math import *

no1 = int(input('enter the first integer'))
no2 = int(input('enter the second integer'))
no3 = int(input('enter the third integer'))

print(f'{min(no1, no2, no3)},{(no1 + no2 + no3) - (min(no1, no2, no3) + (max(no1, no2, no3)))},{max(no1, no2, no3)}')
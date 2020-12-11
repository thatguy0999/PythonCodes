from turtle import *
from random import randint

speed('fastest')
def polygon(sides, length):
    for i in range(sides):
        forward(length)
        left(360/sides)

while True:
    sides = input('how many sides?')
    try:
        sides = int(sides)
        if sides <= 2:
            print('please enter a valid input')
        
        elif sides > 2:
            sides = int(sides)
            break
            
    except:
        if sides == 'random':
            sides = randint(3,12)
            break
            
        else:
            print('please enter a valid input')

while True:
    length = input('what will be the length of each side?')
    try:
        length = float(length)
        if length <= 0:
            print('please enter a valid input')
        
        elif length > 0:
            break
            
    except:
        if length == 'random':
            length = randint(30,150)
            break
            
        else:
            print('please enter a valid input')
while True:
    hue = input('what is the colour of the polygon')
    try:
        color('black',hue)
        break
              
    except:
        if hue == 'random':
            colormode(255)
            fillcolor(randint(0,255),randint(0,255),randint(0,255))
        
        else:
            print('please enter a valid input')

begin_fill()
polygon(sides, length)
end_fill()
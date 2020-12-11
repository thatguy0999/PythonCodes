from turtle import *
from random import choice, randrange

colors = ['yellow', 'indigo', 'blue','violet','orange','green','red']

bgcolor(choice(colors))
speed('fastest')
penup()
goto(-450,320)
pendown()

def randtri():
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()
    
def randtri_row():
    for i in range(9):
        randtri()
        penup()
        forward(100)
        pendown()

for i in range(4):
    #h = randrange(len(colors))
    #color('black',colors[h])
    #colors.pop(h)
    r1 = choice(colors)
    color('black', r1)
    colors.remove(r1)
    randtri_row()
    penup()
    right(90)
    forward(100)
    right(90)
    forward(900)
    right(180)
    pendown()

from turtle import *
from random import choice

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

for i in range(8):
    h1 = randint(0,6)

from turtle import *
from random import randint

def random_turtle():
    penup()
    goto(randint(-450,450),randint(-320,320))
    setheading(randint(0,360))
    colormode(255)
    fillcolor(randint(150,255),6,randint(100,150))
    turtlesize(randint(1,10))
    stamp()

shape('turtle')
speed('fastest')
bgcolor('black')
#fillcolor('green')
shapesize(3, 3, 5)

for i in range(50):
    random_turtle()
from turtle import *

bgcolor('violet')
color('black','yellow')

def draw_triangle():
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()

draw_triangle()

        
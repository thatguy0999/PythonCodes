from turtle import *

penup()
goto(-400,320)
pendown()
bgcolor('violet')
color('black','yellow')
speed('fastest')

def triangle():
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()
    
def triangle_row(x, y):
    penup()
    goto(x, y)
    pendown()
    for a in range(8):
        triangle()
        penup()
        forward(100)
        pendown()

for b in range(4):
    triangle_row(-400,320-100*b)

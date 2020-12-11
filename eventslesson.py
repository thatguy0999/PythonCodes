from turtle import *

color('indigo', 'indigo')

def star(): 
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
        done()
    
onkeypress(star,"space")
listen()

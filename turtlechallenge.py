from turtle import *

def polygon(x):
    for i in range(x):
        forward(50)
        right(360/x)
        
polygon(8)
from turtle import *

#variables
#i1 = 30
#x1 = -450
#y1 = 380
#l1 = 750

#settings
speed('fastest')
penup()
goto(-450,380)
pendown()

def fly_to(x,y):
    penup()
    goto(x, y)
    pendown()
    

for i in range(4):
    forward(750)
    right(90)

right(90)

#curve function
#il = interval width
#l1 = length of one side
#x1 = top left x coordinate of box
#y1 = top left y coordinate of box
def curve(i1,l1,x1,y1):
    for a in range(l1//i1):
        fly_to(x1,y1-i1*(1+a))
        goto(x1+i1*(1+a),(y1-l1))
        
    for b in range(l1//i1):
        fly_to(x1+i1*(1+b),(y1-l1))
        goto((x1+l1),((y1-l1)+i1*(1+b)))
        
    for c in range(l1//i1):
         fly_to((x1+l1),((y1-l1)+i1*(1+c)))
        goto((x1+l1)-i1*(1+c),y1)
        
    for d in range(l1//i1):
        fly_to((x1+l1)-i1*(1+d),y1)
        goto(x1,y1-i1*(1+d))

curve(30,750,-450,380)
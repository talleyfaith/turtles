# https://trinket.io/python/5f3994ee28

from turtle import *
from math import *

sq_pen = Turtle() # pen to draw squares
sp_pen = Turtle() # pen to draw spirals

sq_pen.color("red")
sp_pen.color("blue")

ratio = (1 + sqrt(5)) / 2 # golden ratio

def draw_square(pen, side_length):
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)
        
sq_pen.speed(30)
sq_pen.penup()
sq_pen.goto(-190, -190)
sq_pen.pendown()
sq_pen.setheading(90)
size = 233

"""for i in range(8):
    draw_square(sq_pen, size)
    sq_pen.forward(size)
    sq_pen.right(90)
    sq_pen.forward(size)
    size = size/ratio"""

sp_pen.penup()
sp_pen.speed(30)
sp_pen.goto(250, 250)
sp_pen.pendown()
sp_pen.setheading(-90)
radius = 350
for i in range(20):
    sp_pen.circle(-radius, 90)
    radius = radius/ratio

new_pen = Turtle()
new_pen.speed(30)
new_pen.penup()
new_pen.goto(250,250)
new_pen.pendown()
new_pen.setheading(-45)
new_pen.color("green")
radius = 233
for i in range(10):
    new_pen.circle(-radius, 45)
    radius = radius/ratio

pen = Turtle()
pen.penup()
pen.speed(30)
pen.goto(250, 250)
pen.pendown()
pen.set_heading(-45)
pen.color("red")
radius = 233
for i in range(10):
    pen.circle(-radius, 45)
    radius = radius/ratio

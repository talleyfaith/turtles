from turtle import *

def draw_star(x, y, points, size, line, fill):
    penup()
    goto(x, y)
    pendown()

    angle = 180 - (360 / points)
    
    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(size)
        left(angle)
    end_fill()


bgcolor("black")
speed(30)

draw_star(0, 0, 36, 200, "red", "blue")
draw_star(-300, -200, 12, 300, "green", "orange")

done()

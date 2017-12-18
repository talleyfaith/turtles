from turtle import *

line = 'red'
fill = 'yellow'
points = 12
size = 100

angle = 180 - (360 / points)
color(line, fill)
begin_fill()

for i in range(points):
    forward(size)
    left(angle)
    
end_fill()
    
done()

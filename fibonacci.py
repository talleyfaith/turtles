# https://trinket.io/python/5f3994ee28

from turtle import *
from math import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pen = Turtle()

colormode(255)

ratio = (1 + sqrt(5)) / 2 # golden ratio

def draw_square(side_length):
    for i in range(4):
        forward(side_length)
        right(90)

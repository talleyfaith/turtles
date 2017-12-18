import random
from turtle import *

justin = Turtle()
jaden = Turtle()
annie = Turtle()

justin.shape("turtle")
justin.color("green")

jaden.shape("turtle")
jaden.color("red")

annie.shape("turtle")
annie.color("blue")

jaden.forward(50)

for i in range(10):
    annie.left(53)
    justin.right(36)
    annie.forward(11)
    justin.forward(50)

jaden.left(90)

all_turtles = [justin, jaden, annie]

while True:
    for t in all_turtles:
        rand_dir = random.randint(-20, 20)
        rand_dist = random.randint(5, 10)

        t.right(rand_dir)
        t.forward(rand_dist)



    

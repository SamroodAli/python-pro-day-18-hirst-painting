import colorgram
from turtle import Turtle, Screen
from random import choice

from collections import namedtuple
colors = colorgram.extract("images/image.jpg", 35)
colors_tuples = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_tuples.append((r, g, b))

# code for turtle
t = Turtle()
# code for screen
scr = Screen()
scr.colormode(255)
t.penup()
t.hideturtle()
t.speed(0)

# code to set custom x and y co-ordinate
sety = -200
t.setposition(-200, -200)
for position in range(1, 101):
    color = choice(colors_tuples)
    t.dot(20, color)
    t.forward(50)
    if position % 10 == 0:
        sety += 50
        t.setposition(-200, sety)


scr.exitonclick()

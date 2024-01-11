import random
import turtle as t
from turtle import Screen

sefa = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]
sefa.pensize(10)
sefa.speed(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c


sefa.pendown()
sefa.forward(1)

screen = Screen()
screen.exitonclick()

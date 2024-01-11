import random
import turtle as t
from turtle import Screen
import Turtle_Drawing_Colorgram

sefa = t.Turtle()
t.colormode(255)
sefa.speed(10)
sefa.penup()
pos = -200
step = 50
sefa.goto(pos, pos)
row = 10
sefa.hideturtle()

for a in range(row):
    for i in range(row):
        color = Turtle_Drawing_Colorgram.random_color()
        sefa.dot(20, color)
        sefa.forward(step)
    sefa.setposition(pos, pos + ((a + 1) * step))

screen = Screen()
screen.exitonclick()

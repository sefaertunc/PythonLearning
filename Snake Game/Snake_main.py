import time
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = []

for i in range(3):
    part = Turtle("square")
    part.color("white")
    part.turtlesize(1, 1)
    part.penup()
    part.setposition(i * -20, 0)
    snake.append(part)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake:
        segment.forward(20)


screen.exitonclick()

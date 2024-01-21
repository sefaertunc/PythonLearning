from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

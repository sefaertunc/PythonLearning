from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_LENGTH = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(0, -280)
        self.speed = MOVE_DISTANCE

    def move_upward(self):
        self.forward(self.speed)

    def check_winning_line(self):
        if self.ycor() > FINISH_LINE_LENGTH:
            return "y"
        return "n"

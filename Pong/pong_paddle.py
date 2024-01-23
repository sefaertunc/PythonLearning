from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, corX, corY, index):
        super().__init__()
        self.length = 5
        self.index = index
        self.shape("square")
        self.color("white")
        self.shapesize(self.length, 1)
        self.penup()
        self.goto(corX, corY)

    def move_upward(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_downward(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

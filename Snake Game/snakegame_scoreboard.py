from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 275)
        self.display_score()

    def display_score(self):
        self.write(f"Score = {self.score}", align="center", font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=('Arial', 18, 'bold'))


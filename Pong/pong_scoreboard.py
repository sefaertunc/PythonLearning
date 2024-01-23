from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.winner_score = 10
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 70, "bold"))

    def increase_score(self, player):
        if player == "r":
            self.right_score += 1
            self.update_score()
        elif player == "l":
            self.left_score += 1
            self.update_score()

    def check_winner(self):
        if self.left_score == self.winner_score or self.right_score == self.winner_score:
            return False
        return True

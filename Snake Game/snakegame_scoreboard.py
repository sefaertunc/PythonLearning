from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 275)
        self.display_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.high_score = self.get_high_score()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score} I High Score: {self.high_score}", align="center",
                   font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def save_high_score(self):
        with open("snakegame_database.txt", "w") as file:
            file.write(str(self.high_score))

    @staticmethod
    def get_high_score():
        with open("snakegame_database.txt", "r") as file:
            high_score = int(file.read())
            return high_score

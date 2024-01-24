from turtle import Screen


class ScreenMaker:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Crossing Road")
        self.screen.bgcolor("white")
        self.screen.setup(600, 600)
        self.screen.tracer(0)

    def screen_listen(self, user):
        self.screen.listen()
        self.screen.onkeypress(user.move_upward, "Up")

    def screen_exit(self):
        self.screen.exitonclick()

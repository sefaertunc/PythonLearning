from turtle import Screen


class ScreenMaker:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(800, 600)
        self.screen.tracer(0)

    def screen_listen(self, user):
        self.screen.listen()
        if user.index == "r":
            self.screen.onkey(user.move_upward, "Up")
            self.screen.onkey(user.move_downward, "Down")
        elif user.index == "l":
            self.screen.onkey(user.move_upward, "w")
            self.screen.onkey(user.move_downward, "s")

    def screen_exit(self):
        self.screen.exitonclick()

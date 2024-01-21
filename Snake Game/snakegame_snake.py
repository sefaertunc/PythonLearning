from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for i in range(3):
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.setposition(i * -MOVE_DISTANCE, 0)
            self.snake_list.append(part)

    def move_snake(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            pos_x = self.snake_list[snake_num - 1].xcor()
            pos_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].setposition(pos_x, pos_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        part = Turtle("square")
        part.color("white")
        part.penup()
        pos = self.snake_list[-1].position()
        part.setposition(pos)
        self.snake_list.append(part)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def detect_collision_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < - 280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def detect_collision_snake(self):
        for part in self.snake_list[1:]:
            if self.head.distance(part) < 10:
                return True

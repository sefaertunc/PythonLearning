import random
from turtle import Turtle

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'grey']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CONST_CHANCE = 85


class CarManager:
    def __init__(self, player):
        self.car_list = []
        self.player = player

    def car_spawner(self):
        chance = random.randint(1, 100)
        if chance > CONST_CHANCE:
            car = Car()
            self.car_list.append(car)
        else:
            pass

    def car_movement(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def check_collision(self):
        result = True
        for car in self.car_list:
            if car.distance(self.player) < 20:
                result = False
        return result


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.identify_color()
        self.identify_start_position()

    def identify_color(self):
        color = random.choice(colors)
        self.color(color)

    def identify_start_position(self):
        x_pos = 300
        random_y = random.randint(-250, 250)
        self.setposition(x_pos, random_y)

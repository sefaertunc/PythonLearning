import time
from turtle import Screen
from snakegame_snake import Snake
from snakegame_food import Food
from snakegame_scoreboard import Scoreboard

# Screen Adjustment
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.move_food()
        snake.add_segment()
        scoreboard.increase_score()

    if snake.detect_collision_wall() or snake.detect_collision_snake():
        scoreboard.game_over()
        is_game_on = False


screen.exitonclick()

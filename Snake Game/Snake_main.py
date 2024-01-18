import time
from turtle import Screen
from snakegame_snake import Snake

# Screen Adjustment
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

is_game_on = True
a = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()

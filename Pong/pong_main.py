import time

from pong_ball import Ball
from pong_screen import ScreenMaker
from pong_paddle import Paddle

main_screen = ScreenMaker()
right_paddle = Paddle(350, 0, "r")
left_paddle = Paddle(-350, 0, "l")
ball = Ball()
print(left_paddle.pos())
game_is_on = True
while game_is_on:
    main_screen.screen.update()
    ball.move_ball()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.detect_wall()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.detect_ball()








    main_screen.screen_listen(right_paddle)
    main_screen.screen_listen(left_paddle)
main_screen.screen_exit()

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
    ball.detect_wall()
    ball.detect_ball(right_paddle)
    ball.detect_ball(left_paddle)



    main_screen.screen_listen(right_paddle)
    main_screen.screen_listen(left_paddle)
main_screen.screen_exit()

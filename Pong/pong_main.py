from pong_ball import Ball
from pong_screen import ScreenMaker
from pong_paddle import Paddle
from pong_scoreboard import Scoreboard

main_screen = ScreenMaker()
right_paddle = Paddle(350, 0, "r")
left_paddle = Paddle(-350, 0, "l")
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    main_screen.screen.update()
    ball.move_ball()
    ball.detect_wall()
    ball.detect_paddle(right_paddle)
    ball.detect_paddle(left_paddle)
    ball.check_missing(scoreboard, right_paddle, left_paddle)
    game_is_on = scoreboard.check_winner()

    main_screen.screen_listen(right_paddle)
    main_screen.screen_listen(left_paddle)
main_screen.screen_exit()

import time

from crossing_road_screen import ScreenMaker
from crossing_road_player import Player
from crossing_road_car import CarManager

main_screen = ScreenMaker()
player = Player()
car_manager = CarManager(player)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    main_screen.screen.update()
    car_manager.car_spawner()
    car_manager.car_movement()
    is_game_on = car_manager.check_collision()

    result = player.check_winning_line()
    if result == "y":
        is_game_on = False

    main_screen.screen_listen(player)
main_screen.screen_exit()

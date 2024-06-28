import turtle as t
import colorgram
from hirst_back import HirstBase

colors = colorgram.extract('mario.jpg', 10)
base_game = HirstBase(10, 50)

base_game.create_dots(colors=colors)

screen = t.Screen()
screen.exitonclick()

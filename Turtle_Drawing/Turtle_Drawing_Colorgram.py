import colorgram
import random

colors = colorgram.extract('pacman.jpg', 12)


def random_color():
    index = random.randint(0, len(colors) - 1)
    r = colors[index].rgb.r
    g = colors[index].rgb.g
    b = colors[index].rgb.b
    random_c = (r, g, b)
    return random_c

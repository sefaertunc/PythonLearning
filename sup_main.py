def divide_numbers(a, b):
    return a / b


def draw_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '*')

draw_christmas_tree(10)
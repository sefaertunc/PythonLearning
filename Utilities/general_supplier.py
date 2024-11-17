import random


class GeneralSupplier:
    def __init__(self):
        self.__alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.__numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__symbols = ['+', '-', '*', '/', '?', '%', '&', ')', '(', '#', '!', '=', '$', '@', ]
        self.__names = ["Javier", "Anna", "Cherokee", "Betsy", "Tatyana", "Zack", "Amanda", "Miracle", "Devin", "Ciel"]
        self.__objects = ["flashlight", "shoe lace", "squirt gun", "packet of seeds", "pants", "lighter",
                          "box of baking soda", "mobile phone", "bottle cap", "chocolates", "whip", "plastic fork",
                          "comb", "spool of ribbon", "wine glass", "house", "desk", "glass", "ice cube", "apple",
                          "can of whipped cream", "rusty nail", "mp3 player", "balloon", "CD", "coffee mug",
                          "extension cord", "rat", "banana"]
        self.__color = ["red", "green", "yellow", "blue", "magenta", "orange", "black", "white"]

    def get_random_color(self):
        return random.choice(self.__color)

    def get_color_by_index(self, number):
        return self.__color[number]

    def get_random_letter(self):
        return random.choice(self.__alphabet)

    def get_letter_by_index(self, number):
        return self.__alphabet[number]

    def get_random_symbol(self):
        return random.choice(self.__symbols)

    def get_symbol_by_index(self, number):
        return self.__symbols[number]

    def get_random_number(self):
        return random.choice(self.__numbers)

    def get_number_by_index(self, number):
        return self.__numbers[number]

    def get_random_object(self):
        return random.choice(self.__objects)

    def get_object_by_index(self, number):
        return self.__objects[number]

    def get_random_name(self):
        return random.choice(self.__names)

    def get_name_by_index(self, number):
        return self.__names[number]

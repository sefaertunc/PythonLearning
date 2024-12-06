import random


class GeneralSupplier:
    def __init__(self):
        self.__alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        self.__numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__symbols = [
            '+', '-', '*', '/', '%', '=', '&', '!', '?', '#', '@', '$', '^', '(', ')', '_', ':', ';', '.'
        ]
        self.__names = [
            "Javier", "Anna", "Cherokee", "Betsy", "Tatyana", "Zack", "Amanda", "Miracle", "Devin", "Ciel",
            "Liam", "Olivia", "Noah", "Emma", "Ethan", "Sophia", "Lucas", "Mia", "Jackson", "Ava",
            "Sebastian", "Isabella", "Mateo", "Aria", "Aiden", "Amelia", "Elijah", "Harper", "Benjamin", "Luna",
            "Henry", "Ella", "James", "Layla", "Alexander", "Scarlett", "Michael", "Grace", "William", "Chloe",
            "Gabriel", "Ellie", "Carter", "Lillian", "Daniel", "Hannah", "Caleb", "Addison", "Wyatt", "Zoey",
            "Julian", "Madison", "Jayden", "Violet", "Nathan", "Penelope", "Isaac", "Aurora", "Ryan", "Brooklyn",
            "Sofia", "Victoria", "Elizabeth", "Leo", "Maxwell", "Diana", "Victor", "Ivy", "Theo", "Eliza",
            "Eleanor", "Reese", "Hazel", "Lila", "Sienna", "Quinn", "Arabella", "Freya", "Aurélie", "Dimitri"
        ]

        self.__objects = [
            "flashlight", "shoe lace", "squirt gun", "packet of seeds", "pants", "lighter",
            "box of baking soda", "mobile phone", "bottle cap", "chocolates", "whip", "plastic fork",
            "comb", "spool of ribbon", "wine glass", "house", "desk", "glass", "ice cube", "apple",
            "can of whipped cream", "rusty nail", "mp3 player", "balloon", "CD", "coffee mug",
            "extension cord", "rat", "banana", "toothbrush", "keychain", "backpack", "candle",
            "headphones", "notebook", "paperclip", "water bottle", "umbrella", "scissors", "towel",
            "blanket", "toy car", "watch", "pencil", "eraser", "knife", "jar", "basket", "tissue box"
        ]

        self.__color_dict = {
            "red": "#F28B82",
            "green": "#B9E3B1",
            "yellow": "#FFF9C4",
            "blue": "#AECBFA",
            "magenta": "#F8BBD0",
            "orange": "#FFD59E",
            "black": "#B0BEC5",
            "white": "#F5F5F5",
            "purple": "#D7BDE2",
            "cyan": "#B2EBF2",
            "pink": "#FDCFE8",
            "brown": "#D7CCC8",
            "gray": "#CFD8DC",
            "teal": "#B2DFDB",
            "beige": "#FFF3E0"
        }

    def get_random_color_name(self):
        return random.choice(list(self.__color_dict.keys()))

    def get_random_color_hex(self):
        return self.__color_dict[random.choice(list(self.__color_dict.keys()))]

    def get_color_hex_by_name(self, name):
        """red, green, yellow, blue, magenta, orange, black, white, purple, cyan, pink, brown, gray, teal, beige"""
        return self.__color_dict[str(name)]

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

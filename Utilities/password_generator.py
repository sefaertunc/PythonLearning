from Utilities import general_supplier
import random

supplier = general_supplier.GeneralSupplier()

class PasswordGenerator:
    def __init__(self):
        self.__password = []

    def random_password(self, *args):
        """1.letter, 2.number, 3.symbol, Do not enter 4. variable"""
        self.__password.clear()
        for _ in range(args[0]):
            self.__password += supplier.get_random_letter()

        for _ in range(args[1]):
            self.__password += supplier.get_random_number()

        for _ in range(args[2]):
            self.__password += supplier.get_random_symbol()

        random.shuffle(self.__password)
        demo_password = "".join(self.__password)
        return demo_password
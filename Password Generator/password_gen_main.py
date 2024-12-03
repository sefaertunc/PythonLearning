from Utilities import general_supplier
import random as rand

supplier = general_supplier.GeneralSupplier()

num_letters = int(input("How many letters do want to add ?"))
num_digits = int(input("How many digits do you want to add ?"))
num_symbols = int(input("How many symbols do you want to add ?"))

password = []

for numb in range(num_letters):
    password += supplier.get_random_letter()

for numb in range(num_digits):
    password += supplier.get_random_number()

for numb in range(num_symbols):
    password += supplier.get_random_symbol()

rand.shuffle(password)

password = "".join(password)

print(f"Your password is: {password}")
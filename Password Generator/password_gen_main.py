import general_supplier as supplier
import random as rand

num_letters = int(input("How many letters do want to add ?"))
num_digits = int(input("How many digits do you want to add ?"))
num_symbols = int(input("How many symbols do you want to add ?"))

password = []

for numb in range(num_letters):
    password += rand.choice(supplier.alphabet)

for numb in range(num_digits):
    password += rand.choice(supplier.numbers)

for numb in range(num_symbols):
    password += rand.choice(supplier.symbols)

rand.shuffle(password)

password = "".join(password)

print(f"Your password is: {password}")
import random
import pandas

with open("../../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    sample_names = [names.strip() for names in names.readlines()]

names_with_nums = {name: random.randint(1, 100) for name in sample_names}
print(names_with_nums)
bigger_than_50_names = {name: num for (name, num) in names_with_nums.items() if num > 50}
print(bigger_than_50_names)

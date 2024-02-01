numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Sefa"
new_name = [letter for letter in name]
print(new_name)

sample_range = range(1, 5)
new_range = [number * 2 for number in sample_range]
print(new_range)

new_range2 = [number for number in numbers if number % 2 == 0]
print(new_range2)

with open("../../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    sample_names = names.readlines()

sample_names_list = [names.strip() for names in sample_names]
print(sample_names_list)

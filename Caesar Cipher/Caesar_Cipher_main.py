from alphabet import alphabet_list


def caesar(text_message, var_direction, var_shift):
    modified_text = ""
    for letter in text_message:
        if letter in alphabet_list:
            position = alphabet_list.index(letter)
            new_position = 0
            if var_direction == "encode":
                if (position + var_shift) > len(alphabet_list) - 1:
                    new_position = (position +
                                    (var_shift % len(alphabet_list))) - len(alphabet_list)
                else:
                    new_position = position + var_shift
            elif var_direction == "decode":
                new_position = position - var_shift % len(alphabet_list)
            modified_text += alphabet_list[new_position]
        else:
            modified_text += letter
    print(f"The {var_direction}d text is {modified_text}")


program_check = True

while program_check:

    direction = input("\nEncode or Decode:\n").lower()

    if direction == "encode" or direction == "decode":
        message = input("Type your message:\n").lower()
        shift = int(input("Type shift number:\n"))
        caesar(message, direction, shift)
    else:
        print("Wrong instruction !!")

    program = input("Do you want to try again? Y/N\n").lower()
    if program == "y":
        program_check = True
    elif program == "n":
        program_check = False
    else:
        program_check = False

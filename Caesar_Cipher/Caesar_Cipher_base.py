from alphabet import alphabet_list

class Caesar_Cipher(object):
    def __init__(self):
        self.message = ""
        self.direction = ""
        self.shift = 0

    def enter_cryption(self):
        direction = input("\nEncode or Decode:\n").lower()
        if direction == "encode" or direction == "decode":
            self.direction = direction
            self.enter_message()
            self.enter_shift()
            self.caesar_cipher()
        else:
            print("Wrong instruction !!")

    def enter_message(self):
        self.message = input("Type your message:\n").lower()

    def enter_shift(self):
        self.shift = int(input("Type shift number:\n"))

    def caesar_cipher(self):
        modified_text = ""
        for letter in self.message:
            if letter in alphabet_list:
                position = alphabet_list.index(letter)
                new_position = 0
                if self.direction == "encode":
                    if (position + self.shift) > len(alphabet_list) - 1:
                        new_position = (position + (self.shift % len(alphabet_list))) - len(alphabet_list)
                    else:
                        new_position = position + self.shift
                elif self.direction == "decode":
                    new_position = position - self.shift % len(alphabet_list)
                modified_text += alphabet_list[new_position]
            else:
                modified_text += letter
        print(f"The {self.direction}d text is '{modified_text}'")

    def check_game(self):
        program = input("Do you want to try again? Y/N\n").lower()
        if program == "y":
            self.clear_data()
            return True
        elif program == "n":
            return False
        else:
            return False

    def clear_data(self):
        self.message = ""
        self.direction = ""
        self.shift = 0


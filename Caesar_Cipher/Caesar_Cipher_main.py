from Caesar_Cipher_base import Caesar_Cipher

the_game = Caesar_Cipher()
program_check = True

while program_check:
    the_game.enter_cryption()
    program_check = the_game.check_game()

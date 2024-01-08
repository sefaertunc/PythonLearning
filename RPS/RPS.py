import random

shapes = ["Rock", "Paper", "Scissors"]
base3 = ["1", "2", "3"]
player_input = input("Choose: Rock=1, Paper=2, Scissors=3\n")
if (player_input != base3[int(player_input) - 1]):
  print("Invalid input !!!")
else:
  player_index = int(player_input) - 1

  if (player_index == 0 or player_index == 1 or player_index == 2):
    computer_index = random.randrange(3)
    computer_hand = shapes[computer_index]
    player_hand = shapes[player_index]
    print(f"You select {player_hand}")
    print(f"Computer selects {computer_hand}")

    if (player_index != computer_index):
      if (player_index != computer_index):
        if (player_index == 0):
          if (computer_index == 1):
            print("You lost")
          else:
            print("You won")
        elif (player_index == 1):
          if (computer_index == 0):
            print("You win")
          else:
            print("You lost")
        else:
          if (computer_index == 0):
            print("You lost")
          else:
            print("You won")
      else:
        print("It's draw")
    else:
      print("It's draw")
  else:
    print("Invalid input, you lost")

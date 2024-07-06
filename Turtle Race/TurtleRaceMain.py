import random
from TurtleRaceBack import CreateTurtle
import turtle as t
from Utilities import general_supplier

screen = t.Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")
turtle_list = []
supplier = general_supplier.GeneralSupplier()

end_race = False

for i in range(5):
	turtle = CreateTurtle(color=supplier.get_color_by_index(i), pos=(-200, 50*(2-i)))
	turtle_list.append(turtle)


while not end_race:
	for cop in turtle_list:
		if cop.xcor() > 215:
			end_race = True
			if user_bet == cop.pencolor():
				print("You guessed right!")
			else:
				print("You guessed wrong!")
		step = random.randint(1, 10)
		cop.move_forward(speed=step)


screen.exitonclick()

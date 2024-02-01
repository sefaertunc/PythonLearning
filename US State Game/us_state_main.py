import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer = screen.textinput(f"{len(guessed_states)}/{len(all_states)} States Correct",
                              "What's your state's name?").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        name.color("Black")
        temp_state = states_data[states_data.state == answer]
        name.setpos(int(temp_state.x), int(temp_state.y))
        name.write(temp_state.state.item())
        guessed_states.append(answer)

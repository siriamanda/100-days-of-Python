import turtle
import pandas as pd
from state_names import StateNames

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
current_score = 0

while game_is_on:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)

    state_data = pd.read_csv("50_states.csv")
    state_list = state_data.state.to_list()

    if answer_state in state_data.state.values:
        state_info = state_data[state_data.state == answer_state]

        state_guess = StateNames(state_info)
        state_guess.write_state()


screen.exitonclick()


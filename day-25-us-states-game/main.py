import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")
state_list = state_data.state.to_list()

correct_guesses = []
current_score = 0

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{current_score}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_states = [state for state in state_list if state not in correct_guesses]
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        state_info = state_data[state_data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer_state, align="center", font=("Arial", 12, "bold"))

        correct_guesses.append(answer_state)
        current_score = len(correct_guesses)

screen.exitonclick()

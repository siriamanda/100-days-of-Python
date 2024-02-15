from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data_file = pd.read_csv("data/french_words.csv")
word_dict_list = data_file.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #

def next_card():
    random_selection = random.choice(word_dict_list)
    french_word = random_selection["French"]
    english_word = random_selection["English"]
    canvas.itemconfig(word_label, text=french_word)
    canvas.itemconfig(language_label, text="French")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language_label = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word_label = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

# ---------------------------- FLASH CARD ------------------------------- #

next_card()

# random_word = data_file.French.sample()
# print(random_word)

window.mainloop()

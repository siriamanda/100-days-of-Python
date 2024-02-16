from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data_file = pd.read_csv("data/french_words.csv")
word_dict_list = data_file.to_dict(orient="records")
random_selection = {}

# ---------------------------- FUNCTIONS ------------------------------- #

def next_card():
    global random_selection, flip_timer
    window.after_cancel(flip_timer)
    random_selection = random.choice(word_dict_list)
    french_word = random_selection["French"]
    canvas.itemconfig(word_label, text=french_word, fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = random_selection["English"]
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front)
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

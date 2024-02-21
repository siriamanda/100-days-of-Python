from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_selection = {}
word_dict_list = {}

try:
    data_file = pd.read_csv("data/words_to_learn_swedish.csv")
except FileNotFoundError:
    original_file = pd.read_csv("data/swedish_words.csv")
    word_dict_list = original_file.to_dict(orient="records")
else:
    word_dict_list = data_file.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #


def next_card():
    global random_selection, flip_timer, word_dict_list
    window.after_cancel(flip_timer)
    random_selection = random.choice(word_dict_list)
    swedish_word = random_selection["Swedish"]
    canvas.itemconfig(word_label, text=swedish_word, fill="black")
    canvas.itemconfig(language_label, text="Swedish", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global random_selection
    english_word = random_selection["English"]
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    global random_selection, word_dict_list
    word_dict_list.remove(random_selection)
    next_card()
    data = pd.DataFrame(word_dict_list)
    data.to_csv("data/words_to_learn_swedish.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()     # Create UI window
window.title("Flashy")     # Name the window
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)      # After 3 seconds the function flip_card is processed

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
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# ---------------------------- FLASH CARD ------------------------------- #

next_card()

window.mainloop()

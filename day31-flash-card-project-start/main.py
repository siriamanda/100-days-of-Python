from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front = PhotoImage(file="/Users/sraaf/Documents/src/100-days-of-Python/day31-flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="/Users/sraaf/Documents/src/100-days-of-Python/day31-flash-card-project-start/images/card_back.png")
right = PhotoImage(file="/Users/sraaf/Documents/src/100-days-of-Python/day31-flash-card-project-start/images/right.png")
wrong = PhotoImage(file="/Users/sraaf/Documents/src/100-days-of-Python/day31-flash-card-project-start/images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)



window.mainloop()

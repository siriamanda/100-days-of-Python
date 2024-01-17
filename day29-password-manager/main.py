from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry boxes

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons

generate_password_button = Button(text="Generate Password", width=13)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
import pandas as pd
import random as r
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# Check to see if words_to_learn file is created
try:
    learn_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    data_dict = data.to_dict(orient="records")
else:
    data_dict = learn_data.to_dict(orient="records")


# Function for card functionally
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = r.choice(data_dict)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip)


# Function to flip card
def flip():
    global current_card
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=current_card["English"], fill='white')


# If card is known then remove from words_to_learn and save
def known():
    global current_card
    data_dict.remove(current_card)
    to_learn = pd.DataFrame(data_dict)
    to_learn.to_csv('data/words_to_learn.csv', index=False)


# UI Set Up
window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text='', fill='black', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='', fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, bd=0, borderwidth=0, border=0,
                      command=lambda:[next_card(), known()])
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, borderwidth=0, border=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()



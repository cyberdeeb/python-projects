import pandas as pd
import random as r
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def random_word():
    data = pd.read_csv('data/french_words.csv')
    data_dict = data.to_dict(orient="records")
    index = r.randint(1, len(data)-1)
    french_word = data_dict[index]['French']
    canvas.itemconfig(word, text=f'{french_word}')
    

# UI Set Up
window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text='French', fill='black', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='French', fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, bd=0, borderwidth=0, border=0, command=random_word)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, borderwidth=0, border=0, command=random_word)
wrong_button.grid(column=1, row=1)





window.mainloop()



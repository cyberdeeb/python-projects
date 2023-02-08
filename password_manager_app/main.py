import csv
import pyperclip
import random
from tkinter import *
from tkinter import messagebox


# Password generator function
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Loops to form password
    rand_letter = [random.choice(letters) for letter in range(random.randint(8, 10))]
    rand_symbol = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    rand_number = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password = rand_letter + rand_number + rand_symbol

    # Shuffle password string
    rand_password = ''.join(random.sample(password, len(password)))

    # Insert password into field
    password_entry.insert(0, rand_password)

    # Copy generated password and allow user to paste
    pyperclip.copy(rand_password)


# Save data function
def save():

    # Get values from entry widgets
    site = website_entry.get()
    user = eun_entry.get()
    pw = password_entry.get()

    # Ensure that fields are not blank
    if site == '' or pw == '' or user == '':
        # If blank then show this message box
        messagebox.showwarning(title='Error', message="Please don't leave any feilds empty!")
    else:
        # If filled, then allow user to review
        is_ok = messagebox.askokcancel(title=f'{site}', message=f'These are the details entered: \nEmail: {user} \nPassword: {pw} '
                                               f'\nIs it ok to save?')
        # Append data to CSV file
        if is_ok:
            with open('data.csv', mode='a') as file:
                fieldnames = ['website', 'email/username', 'password']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({'website':site, 'email/username':user, 'password':pw})

            # Clear fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI Set Up
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text='Website:')
website.grid(column=0, row=1)
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)

eun = Label(text='Email/Username:')
eun.grid(column=0, row=2)
eun_entry = Entry(width=38)
eun_entry.focus()
eun_entry.insert(0, 'pokemaster@gmail.com')
eun_entry.grid(column=1, row=2, columnspan=2)

password = Label(text='Password:')
password.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate = Button(text='Generate Password', command=generate_password)
generate.grid(column=2, row=3)

add = Button(text='Add', width=36, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()

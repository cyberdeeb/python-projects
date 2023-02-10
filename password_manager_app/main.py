import json
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
    new_data = {
        site: {
            'email':user,
            'password':pw
        }
    }

    # Ensure that fields are not blank
    if site == '' or pw == '' or user == '':
        # If blank then show this message box
        messagebox.showwarning(title='Error', message="Please don't leave any fields empty!")
    else:
        # Check if file has been created & append data to JSON file:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating file with new data
            data.update(new_data)

            # Saving the updated file
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)

            # Clear fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def find():

    # Get the site the user is searching for
    site = website_entry.get()

    try:
        with open('data.json', mode='r') as file:
            # Reading data
            data = json.load(file)
    # If file doesn't exist
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message="You haven't saved any passwords yet!")
    else:
        # Search through the loaded data
        try:
            password = data[site]['password']
            email = data[site]['email']
        # If search values do not exist
        except KeyError:
            messagebox.showwarning(title='Error', message=f"No details for {site} exist.")
        # Pop up message providing details to the user
        else:
            messagebox.showinfo(title=f'{site}', message=f'Email: {email}\n Password: {password}')


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)

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

search = Button(text='Search', width=13, command=find)
search.grid(column=2, row=1)


window.mainloop()

#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize password and its length
password = ''
password_length = nr_letters + nr_numbers + nr_symbols

# Loops to form password
for letter in range(1, nr_letters + 1):
  rand_letter = random.choice(letters)
  password += rand_letter

for symbol in range(1, nr_symbols + 1):
  rand_symbol = random.choice(symbols)
  password += rand_symbol

for number in range(1, nr_numbers + 1):
  rand_number = random.choice(numbers)
  password += rand_number

# Shuffle password string
rand_password = ''.join(random.sample(password, password_length))

print(rand_password)

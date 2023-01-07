from art import logo

# Initialize variables
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rerun = True

# Function that will encode or decode message based on user inputs
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # Covers decode
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # Will only edit letters (not symbols, spaces, or numbers)
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
#Print the logo when the program starts.
print(logo)

# While loop to check if program should be rerun
while rerun == True:
  
  text = input("Type your message:\n").lower()

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  # Loop to verify that user only inputs encode or decode
  while direction not in ['encode','decode']:
    direction = input("Invalid choice. Please type 'encode' to encrypt, type 'decode' to decrypt:\n")

  # Loop to ensure that shift is an integer
  while True:
    try:
      shift = int(input("Type the shift number:\n"))
    except ValueError:
      print('Please enter a valid number.')
    else:
      break

  # Will allow for shift inputs greater than 26
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  end_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  
  if end_cipher == 'no':
    rerun = False
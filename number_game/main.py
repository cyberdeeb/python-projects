#Number Guessing Game Objectives:
import random
from art import logo
from replit import clear

# ASCII art logo
print(logo)
print('Welcome to the guessing game!')
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,101)

# Loop to ensure user picks on of the two difficulties
while True:
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
  if level not in ['easy','hard']:
    print("Please choose between the two difficulties. Type 'easy' or 'hard'")
    clear()
  else:
    break
    
# Set lives based on level chosen
if level == 'easy':
    lives = 10
else:
    lives = 5

# Loop until user has ran out of lives
while lives > 0:
  print(f'You have {lives} attempts remaining to guess the number.')

# Ensure that guess is an integer
  while True:
    try:
      guess = int(input('Make guess: '))
      break
    except ValueError:
      print('Please input a valid number.')

  # Feedback based on guess
  if guess < number:
    print('Too low.')
    lives -= 1
  elif guess > number:
    print('Too high.')
    lives -=1
  else:
    print(f'You did it! The number is {number}!')
    break

# Feedback if user runs out of lives
if lives == 0:
  print(f'You ran out of lives! The number was {number}.')

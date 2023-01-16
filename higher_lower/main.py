from art import logo, vs
from game_data import data
from replit import clear
import random


def main():

  # Initialize variable
  score = 0
  end_game = False
  person_a = random.choice(data)
    
  while not end_game:
    
    print(logo)
    
    person_b = random.choice(data)

    # Ensuring that both choices don't match
    if person_a == person_b:
      person_a = random.choice(data)
    
    print(f'Compare A: {format(person_a)}')
    print(vs)
    print(f'Against B: {format(person_b)}')

    # While loop to make sure user inputs valid choice
    while True:
      choice = input("Who has more followers: Type 'A' or 'B': ").lower().strip()
      if choice not in ['a','b']:
        print("Please input a valid choice.")
      else:
        break
  
    
    match = highest(person_a, person_b, choice)

    # Check to see if user guessed correctly
    if match:
      score += 1
      person_a = person_b
      clear()
    else:
      clear()
      print(f'So close! Your score was {score}')
      end_game = True

  # While loop to make sure user provides a valid input
  while True:
    restart = input("Would you like to play again? Type 'Y' or 'N': ").lower().strip()
    if restart not in ['y','n']:
      print('Please enter a valid input.')
    else:
      break
      
  # Restarting the game
  if restart == 'y':
    score = 0
    clear()
    main()

# Function that will take data from dictionary and format it
def format(person):
  name = person['name']
  description = person['description']
  country = person['country']
  return f'{name}, {description}, from {country}'

# Function to check whose follower count is the highest
def highest(person_a, person_b, choice):
  if person_a['follower_count'] > person_b['follower_count']:
    return choice == "a"
  else: 
    return choice == "b"

main()
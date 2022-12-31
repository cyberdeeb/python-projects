import random

# Game images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

bomb = '''
      ,--.!,
     __/   -*-
   ,d08b.  '|`
   0088MM     
   `9MMP'     
'''

print('Welcome to Rock, Paper, Scissors!')

choice = int(input('Type 0 for Rock, 1 for Paper, and 2 for Scissors\n'))

# While loop to ensure users input is within parameters
if choice <= 3:

  rps = ['Rock', 'Paper', 'Scissors','Bomb']
  image = [rock, paper, scissors, bomb]

  # Players choice and image
  player_choice = rps[choice]
  player_image = image[choice]

  # Computers choice and image
  computer_choice = rps[random.randint(0,2)]
  computer_image = image[rps.index(computer_choice)]
  
  print(f'You chose: {player_choice}')
  print(player_image)
  
  print(f'The computer chose: {computer_choice}')
  print(computer_image)

  # Winner determination
  if computer_choice == 'Rock' and player_choice == 'Paper':
    print('You win!')
  elif computer_choice == 'Paper' and player_choice == 'Scissors':
    print('You win!')
  elif computer_choice == 'Scissors' and player_choice == 'Rock':
    print('You win!')
  elif computer_choice == 'Scissors' and player_choice == 'Paper':
    print('The computer wins!')
  elif computer_choice == 'Paper' and player_choice == 'Rock':
    print('The computer wins!')
  elif computer_choice == 'Rock' and player_choice == 'Scissors':
    print('The computer wins!')
  elif player_choice == 'Bomb':
    print('You have destroyed everything, you win!')
  else:
    print("It's a tie!")

else:
  print('Please pick a valid number to play this game.')
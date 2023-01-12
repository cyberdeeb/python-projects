import random
from art import logo
from replit import clear

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Initialize values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
end_game = False
users_score = 0
computers_score = 0

# Main function of program
def main(users_score, computers_score):
  print(logo)
  deal_card('both')
  
  users_score = calculate_score(user_cards)
  computers_score = calculate_score(computer_cards)
  end_game = score_check(users_score, computers_score)

  # Loop through to end of program to check and see if user wants to play again
  while True:
    # Loop until end game parameters are met or if user stops drawing cards
    while not end_game:
      print(f'Your cards: {user_cards}')
      print(f'Your score: {users_score}')
      draw_again = input("Would you like to draw another card? Input 'yes' or 'no'.\n" ).lower()
      if draw_again == 'yes':
        clear()
        deal_card('user')
        users_score = calculate_score(user_cards)
        end_game = score_check(users_score, computers_score)
      else:
        # Clear screen for cleaner UI
        clear()
        # Loop to set parameters for computers turn
        while computers_score < 17 and computers_score != 0:
          deal_card('computer')
          computers_score = calculate_score(computer_cards)
        end_game = True
    
    print(f'Your cards: {user_cards}')
    print(f'Your score: {users_score}')

    # Print blank line here
    print("")
    
    print(f'The computers cards: {computer_cards}')
    print(f'The computers score: {computers_score}')

    # Print blank line here
    print("")

    # Compare the scores and check for the winner
    compare(users_score, computers_score)

    # Check if the user wants to play again
    restart = input("Would you like to play again? Input 'yes' or 'no'.\n" ).lower()
    if restart == 'yes':
      user_cards.clear()
      computer_cards.clear()
      clear()
      main(users_score, computers_score)
    elif restart == 'no':
      break
  

# Function that takes whose turn it is as input and then adds cards to list
def deal_card(player):
  if player == 'user':
    user_cards.append(random.choice(cards))
  elif player == 'computer':
    computer_cards.append(random.choice(cards))
  elif player == 'both':
    for i in range(2):
      user_cards.append(random.choice(cards))
      computer_cards.append(random.choice(cards))

#Function that takes a list of cards as input and returns the score. 
def calculate_score(cards_held):
  score = sum(cards_held)
  #if score == 21:
    #return 0
    
  if 11 in cards_held and score > 21:
    cards_held.remove(11)
    cards_held.append(1)
    return sum(cards_held)
  else:
    return score

# Function that takes both scores as inputs and checks end_game parameters
def score_check(users_score, computers_score):
  if users_score > 21:
    return True
  elif users_score == 21:
    return True
  elif computers_score == 21:
    return True
  else:
    return False

    
# Function takes user_score and computer_score and determines the winner
def compare(users_score, computers_score):
  if users_score > 21 or computers_score == 0:
    print('The computer wins!')
  elif computers_score > 21 or users_score == 0:
    print('You win!')
  elif users_score == computers_score:
    print("It's a draw!")
  else:
    if users_score > computers_score:
      print('You win!')
    else:
      print('The computer wins!')


main(users_score, computers_score)

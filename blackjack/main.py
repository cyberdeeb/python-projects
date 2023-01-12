import random
from art import logo
from replit import clear

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
end_game = False

def main(users_score, computers_score):
  print(logo)
  end_game = score_check()
  
  while True:
    while not end_game:
      print(f'Your cards: {user_cards}')
      print(f'Your score: {users_score}')
      draw_again = input("Would you like to draw another card? Input 'yes' or 'no'.\n" ).lower()
      if draw_again == 'yes':
        clear()
        deal_card('user')
        users_score = calculate_score(user_cards)
        # There is a bug here where it does not stop the loop, it will repeat if greater than 21, review
        end_game = score_check()
      else:
        clear()
        while not end_game and computers_score < 17:
          deal_card('computer')
          computers_score = calculate_score(computer_cards)
          end_game = score_check()
        end_game = True
    
    print(f'Your cards: {user_cards}')
    print(f'Your score: {users_score}')
    
    print(f'The computers cards: {computer_cards}')
    print(f'The computers score: {computers_score}')

    compare(users_score, computers_score)
    
    restart = input("Would you like to play again? Input 'yes' or 'no'.\n" ).lower()
    if restart == 'yes':
      clear()
      print(logo)
      main(users_score, computers_score)
    else:
      break
  


def deal_card(player):
  if player == 'user':
    for i in range(1):
      user_cards.append(random.choice(cards))
  elif player == 'computer':
    for i in range(1):
      computer_cards.append(random.choice(cards))
  elif player == 'both':
    for i in range(2):
      user_cards.append(random.choice(cards))
      computer_cards.append(random.choice(cards))

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards_held):
  score = sum(cards_held)
  if len(cards_held) == 2 and score == 21:
    return 0
    
  if 11 in cards_held and score > 21:
    cards_held.remove(11)
    cards_held.append(1)
    return sum(cards_held)
  else:
    return score

def score_check():
  if users_score > 21 or users_score == 0 or computers_score == 0:
    return True

    
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
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

deal_card('both')
  
users_score = calculate_score(user_cards)
computers_score = calculate_score(computer_cards)

main(users_score, computers_score)
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


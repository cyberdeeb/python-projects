from replit import clear
from art import logo


print(logo)
bids = {}

def main():
  
  end_of_bidding = False

  # Loop to run until all users have submitted there bid
  while end_of_bidding == False:
    bidding()
    stop = input('Are there any other bidders? Please type yes or no.\n').lower()

    # Check to see if there are any other bidders
    if stop == 'no':
      # If no, end bidding and clear screen then find winner
      end_of_bidding = True
      clear()
      find_winner()
    else:
      # If yes, clear screen for new user input
      clear()

def bidding():
  name = input('What is your name?\n')
  amount = int(input('What is your bid amount?\n'))

  bids[name] = amount

    
def find_winner():
  amount = 0
  # Loop through dictionary and compare bid amounts to find winner
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > amount:
      amount = bid_amount
  print(f'The winner is {bidder} with a bid of ${amount}!')


main()

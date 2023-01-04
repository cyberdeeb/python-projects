import hangman_art as ha
from hangman_words import word_list
import random
from replit import clear

# Initialize variables used
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Print logo
print(ha.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Loop to create "-"
display = []
for _ in range(word_length):
    display.append("_")

# Loop through game until end_of_game = True (win or loss)
while not end_of_game:

    guess = input("Guess a letter: ").lower()

  # Function to clear console after each guess
    clear()
  
    # if user has entered a letter they've already guessed
    if guess in display:
      print(f'You have already guessed {guess}. Please try again.')
      
    # Check guessed letter and update display if matched
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the word. You have {lives} lives left')
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Display hangman art at each life level
    print(ha.stages[lives])
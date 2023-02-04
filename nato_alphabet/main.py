import pandas as pd

# Read the csv containing data
data = pd.read_csv('nato_phonetic_alphabet.csv')

# Turn the data into a dictionary with letter and nato word
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Get users input and format
word = input('Enter a word: ').strip().upper()

# Create letter list
letters = [letter for letter in word]

# Translate each letter using nato_dict
translate = [nato_dict[letter] for letter in letters]

print(translate)


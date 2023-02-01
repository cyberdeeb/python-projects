# Read lines in name file to create a name list
with open('Input/Names/invited_names.txt') as data:
    name_list = data.readlines()

# For each name take the letter template and create an updated personalized letter
for name in name_list:
    # Strip the \n at the end of the name
    updated_name = name.strip()
    with open(f'Output/ReadyToSend/letter_for_{name}', mode='w') as f1:
        with open('Input/Letters/starting_letter.txt') as f2:
            letter = f2.read()
            new_letter = f1.write(letter.replace('[name]', updated_name))
# Program name
print('Tip Calculator')

# User input values
total = float(input('What was the total of the bill?\n'))

percent = float(input('What tip percentage would you like to give: 10%, 15%, or 20%?\n'))

num_people = float(input('How many people are splitting the bill?\n'))

# Calculation
pay_amount = (total * (percent/100)) / num_people

# Print split amount formatted
print(f'Each person needs to pay: ${pay_amount:.2f}')
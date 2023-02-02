import pandas as pd
import turtle as t

# Screen Set Up
screen = t.Screen()
screen.title('Guess the States!')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

# Pull State and coor data
data = pd.read_csv('50_states.csv')


def main():

    score = 0
    end_game = False
    guessed_states = []
    state_list = data.state.to_list()

    # Loop till game has ended or exit submitted
    while not end_game:
        guess = screen.textinput(title=f'{score}/50 States Correct', prompt='Guess a State!').title()

        # If exit code submitted, break loop and generate csv with missed guesses
        if guess == 'Exit':
            with open('learn.csv', mode='w') as file:
                for state in state_list:
                    file.write(f'{state}\n')
            break

        # Ensure user input is a State and not already guessed
        if guess not in state_list or guess in guessed_states:
            pass
        else:
            # Pull State data from CSV
            state = data[data.state == guess]
            name = state.state.item()
            x = state.x.item()
            y = state.y.item()
            guessed_states.append(guess)
            state_list.remove(name)
            write(name, x, y)
            score += 1

        # End game after all have been guessed
        if score == 50:
            write('YOU GOT THEM ALL!', 0, 300)
            end_game = True


# Function to write
def write(name, x, y):
    text = t.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x, y)
    text.write(f'{name}', font=("Courier", 10, "italic"))


main()

t.mainloop()


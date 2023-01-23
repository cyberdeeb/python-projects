import turtle as t
import random as r

screen = t.Screen()
screen.setup(500, 400)
guess = screen.textinput(title='Who will win?', prompt='Which Turtle will win the race? Enter a color: ')

y = -100

color_list = ['red', 'blue', 'orange', 'purple', 'yellow', 'green']
turtle_list = []

for color in color_list:
    turtle = t.Turtle()
    turtle.penup()
    turtle.shape('turtle')
    turtle.color(color)
    turtle.goto(-230, y)
    turtle_list.append(turtle)
    y += 50

if guess:
    race = True

while race:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if guess == winner:
                print(f'You win! The winner was {winner}')
            else:
                print(f'You lost! The winner was {winner}!')
            race = False
            break
        turtle.forward(r.randint(0, 15))

screen.exitonclick()

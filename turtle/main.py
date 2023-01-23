from colors import c_list
import turtle as t
import random

t.bgcolor('black')
t.colormode(255)
artist = t.Turtle()
artist.penup()
artist.hideturtle()
artist.speed(100)
dot_count = 0
y = 0

while dot_count < 101:
    artist.setheading(225)
    artist.forward(300)
    artist.setheading(0)
    for i in range(10):
        artist.dot(20, random.choice(c_list))
        artist.forward(50)
        dot_count += 1
    artist.setx(0)
    artist.sety(y)
    y += 50




screen = t.Screen()

screen.exitonclick()
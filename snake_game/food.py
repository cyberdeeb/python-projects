from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(.5, .5)
        self.color('blue')
        self.speed('fastest')

        x = r.randint(-270, 270)
        y = r.randint(-270, 270)
        self.goto(x, y)

    def reposition(self):
        x = r.randint(-270, 270)
        y = r.randint(-270, 270)
        self.goto(x, y)
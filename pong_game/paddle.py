from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create(self, position):
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            y_cor = self.ycor()
            y_cor += 50
            self.sety(y_cor)

    def down(self):
        if self.ycor() > -250:
            y_cor = self.ycor()
            y_cor -= 50
            self.sety(y_cor)



from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.color('red')
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y


import turtle as t

# Constant variables
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.snake_list = []
        self.create()
        self.head = self.snake_list[0]

    def create(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = t.Turtle('square')
        snake_segment.color('white')
        snake_segment.speed(SPEED)
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_list.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    #def level_up(self):

    def move(self):
        for segment in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[segment - 1].xcor()
            new_y = self.snake_list[segment - 1].ycor()
            self.snake_list[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

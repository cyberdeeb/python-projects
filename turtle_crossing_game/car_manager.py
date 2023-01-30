from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        rand_chance = r.randint(1, 5)
        if rand_chance == 1:
            car = Turtle()
            car.color(r.choice(COLORS))
            car.shape('square')
            car.shapesize(1, r.randint(2, 5))
            car.penup()
            car.goto(300, r.randint(-240, 240))
            car.setheading(180)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

# Initialize classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key press
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True

# Loop while game is on
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create()
    car_manager.move()

    # Detect if car hits player
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

        # Detect if player passes finish line & increase level
        if player.at_finish_line():
            player.sety(-290)
            scoreboard.calc_score()
            car_manager.level_up()

screen.exitonclick()

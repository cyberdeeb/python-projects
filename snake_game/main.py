import turtle as t
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(0)

end_game = False
x = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while not end_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.calc_score()
        snake.extend()
        food.reposition()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        end_game = True
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            end_game = True
            scoreboard.game_over()

    # Add level up functionality
    #if scoreboard.score > 5:
        #snake.level_up()

screen.exitonclick()

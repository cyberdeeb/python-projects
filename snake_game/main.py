import turtle as t
import random as r
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
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


while not end_game:
    screen.update()
    time.sleep(0.1)


    snake.move()




screen.exitonclick()
import turtle as t
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PONG')

end_game = False

r_paddle = Paddle()
l_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

r_paddle.create((350, 0))
l_paddle.create((-350, 0))

screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')


while not end_game:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.x_bounce()

    # Detect when paddle misses the ball
    if ball.xcor() > 390:
        ball.reposition()
        scoreboard.l_score += 1
        scoreboard.update()

    if ball.xcor() < -390:
        ball.reposition()
        scoreboard.r_score += 1
        scoreboard.update()



screen.exitonclick()

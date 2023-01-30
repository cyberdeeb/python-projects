from turtle import Turtle

FONT = ("Courier", 20, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setpos(-250, 270)
        self.write(f'Level: {self.score}', move=True, font=FONT, align='center')

    def calc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', move=True, font=FONT, align='center')

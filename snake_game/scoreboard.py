from turtle import Turtle

STYLE = ('Courier', 20, 'italic')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        #self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.setpos(0, 270)
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=True, font=STYLE, align=ALIGN)

    def calc_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', move=True, font=STYLE, align=ALIGN)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

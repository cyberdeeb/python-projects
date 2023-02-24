from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"


class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text='Score: 0', bg=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.score.grid(columnspan=2, row=0, padx=10, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.quest_text = self.canvas.create_text(150, 125, text='Question', fill=THEME_COLOR,
                                                  font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(columnspan=2, column=0, row=1)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, borderwidth=0, border=0,
                                  command=self.true_clicked)
        self.true_button.grid(column=0, row=3, pady=20)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, borderwidth=0, border=0,
                                   command=self.false_clicked)
        self.false_button.grid(column=1, row=3, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quest_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quest_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_clicked(self):
        self.feedback(self.quiz.check_answer('True'))

    def false_clicked(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='#77DD77')
        else:
            self.canvas.config(bg='#ff6961')
        self.window.after(1000, func=self.get_next_question)

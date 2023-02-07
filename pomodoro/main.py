import math
from tkinter import *

# Constant Variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARKS = ''
reps = 0
timer_clock = None


# Timer reset function
def reset_time():
    window.after_cancel(timer_clock)
    title.config(text='Timer', fg=GREEN)
    checkmarks.config(text='')
    canvas.itemconfig(timer, text='00:00')
    global reps
    reps = 0


# Timer countdown mechanics
def start_time():
    global reps
    reps += 1

    if reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        title.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title.config(text='Break', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title.config(text='Work')


# Countdown functionality
def countdown(count):

    min_count = math.floor(count / 60)
    sec_count = count % 60

    if sec_count == 0:
        sec_count = "00"
    elif sec_count < 10:
        sec_count = f'0{count}'

    if count >= 0:
        canvas.itemconfig(timer, text=f'{min_count}:{sec_count}')
        global timer_clock
        timer_clock = window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks = ''
        for i in range(math.floor(reps/2)):
            marks += '✓'
        checkmarks.config(text=marks)


# UI set up
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
title.config(pady=20)
title.grid(column=1, row=0)

start = Button(text='Start', relief='flat', highlightthickness=0, borderwidth=0, border=0, bd=0, bg=YELLOW, command=start_time)
start.grid(column=0, row=2)


reset = Button(text='Reset', relief='flat', highlightthickness=0, borderwidth=0, border=0, bd=0, bg=YELLOW, command=reset_time)
reset.grid(column=2, row=2)

checkmarks = Label(text=CHECKMARKS, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
checkmarks.grid(column=1, row=4)


window.mainloop()

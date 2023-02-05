from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=500, height=150)
window.config(padx=100, pady=50)

# Entry
miles = Entry(width=5)
miles.insert(END, string='0')
miles.focus()
miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)

km = Label(text="0", font=("Arial", 24, "bold"))
km.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)


def button_clicked():
    m = float(miles.get())
    calc = round(m * 1.609344, 2)
    km.config(text=calc)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()







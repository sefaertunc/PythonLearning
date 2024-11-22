from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)


def converter():
	distance = float(text_box.get())
	distance *= 1.609344
	kilometer_label['text'] = round(distance, 2)


text_box = Entry(window, width=10)
text_box.place(x=140, y=25)

miles_label = Label(window, text="Miles", font=("Arial", 18))
miles_label.place(x=250, y=25)

equals_label = Label(window, text="is equal to", font=("Arial", 18))
equals_label.place(x=50, y=60)

kilometer_label = Label(window, text="0", font=("Arial", 18))
kilometer_label.place(x=160, y=60)

km_label = Label(window, text="Km", font=("Arial", 18))
km_label.place(x=250, y=60)

button = Button(text="Calculate", command=converter, width=7, height=1, font=("Arial", 14))
button.place(x=140, y=90)

window.mainloop()

import random

import pandas
import pandas as pd
import tkinter as tk
from Utilities import general_supplier

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

supplier = general_supplier.GeneralSupplier()

timer = None
word_card = {}
word_dic_list = {}

try:
	word_file = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
	original_data = pd.read_csv("fcp_data.csv")
	word_dic_list = original_data.to_dict(orient="records")
else:
	word_dic_list = word_file.to_dict(orient="records")


def get_random_word():
	global word_card, flip_timer
	window.after_cancel(flip_timer)
	word_card = random.choice(word_dic_list)
	flash_card_canvas.itemconfig(language_text, text="German", fill="black")
	flash_card_canvas.itemconfig(word_text, text=word_card["German"], fill="black")
	flash_card_canvas.itemconfig(card_background, image=front_image)
	flip_timer = window.after(3000, flip_card)


def flip_card():
	flash_card_canvas.itemconfig(language_text, text="English", fill="white")
	flash_card_canvas.itemconfig(word_text, text=word_card["English"], fill="white")
	flash_card_canvas.itemconfig(card_background, image=back_image)


def know_the_word():
	word_dic_list.remove(word_card)
	data = pandas.DataFrame(word_dic_list)
	data.to_csv("words_to_learn.csv", index=False)
	get_random_word()


window = tk.Tk()
window.title("Flash Card Project")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("900x726")

flip_timer = window.after(3000, flip_card)

flash_card_canvas = tk.Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = tk.PhotoImage(file="images/card_front.png")
back_image = tk.PhotoImage(file="images/card_back.png")
card_background = flash_card_canvas.create_image(400, 263, image=front_image)
flash_card_canvas.grid(row=0, column=0, columnspan=2)

language_text = flash_card_canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill="black")
word_text = flash_card_canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill="black")

right_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
right_button = tk.Button(window, image=right_image, background=BACKGROUND_COLOR, highlightthickness=0,
						 command=lambda: know_the_word())
wrong_button = tk.Button(window, image=wrong_image, background=BACKGROUND_COLOR, highlightthickness=0,
						 command=lambda: get_random_word())
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

get_random_word()

window.mainloop()

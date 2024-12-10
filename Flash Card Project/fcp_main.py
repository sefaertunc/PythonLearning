import random
import pandas as pd
import tkinter as tk
from Utilities import general_supplier

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

supplier = general_supplier.GeneralSupplier()

timer = None
word_dic = None

word_file = pd.read_csv("fcp_data.csv")
word_dic_list = word_file.to_dict(orient="records")


def get_random_word():
	global word_dic
	word_dic = random.choice(word_dic_list)
	flash_card_canvas.itemconfig(language_text, text="German")
	flash_card_canvas.itemconfig(word_text, text=word_dic["German"])
	count_down(3)


def flip_card(word):
	print(word)
	global image
	flash_card_canvas.itemconfig(language_text, text="English", fill="white")
	flash_card_canvas.itemconfig(word_text, text=word["English"], fill="white")
	image = tk.PhotoImage(file="images/card_back.png")
	flash_card_canvas.itemconfig(image, image=image)


def count_down(count):
	global word_dic
	if count > 0:
		global timer
		print(count)
		timer = window.after(1000, count_down, count - 1)
	else:
		flip_card(word_dic)


window = tk.Tk()
window.title("Flash Card Project")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("900x726")

flash_card_canvas = tk.Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = tk.PhotoImage(file="images/card_front.png")
flash_card_canvas.create_image(400, 263, image=image)
flash_card_canvas.grid(row=0, column=0, columnspan=2)

language_text = flash_card_canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill="black")
word_text = flash_card_canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill="black")

right_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
right_button = tk.Button(window, image=right_image, background=BACKGROUND_COLOR, highlightthickness=0,
						 command=lambda: get_random_word())
wrong_button = tk.Button(window, image=wrong_image, background=BACKGROUND_COLOR, highlightthickness=0,
						 command=lambda: get_random_word())
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

get_random_word()

window.mainloop()

import pandas as pd
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

window = tk.Tk()
window.title("Flash Card Project")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("900x726")

flash_card_canvas = tk.Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = tk.PhotoImage(file="images/card_front.png")
flash_card_canvas.create_image(400, 263, image=image)
flash_card_canvas.grid(row=0, column=0, columnspan=1)

language_text = flash_card_canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"), fill="black")
word_text = flash_card_canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"), fill="black")

right_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
right_button = tk.Button(window, image=right_image, background=BACKGROUND_COLOR, highlightthickness=0)
wrong_button = tk.Button(window, image=wrong_image, background=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0, columnspan=2)
right_button.grid(row=1, column=1)

window.mainloop()
